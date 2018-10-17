package com.cbo.util.poi;

import com.cbo.data.handle.DataCaseStrategy;
import com.cbo.data.handle.DataMergeStrategy;
import com.cbo.data.handle.DataSplitStrategy;
import org.apache.poi.hssf.usermodel.HSSFWorkbook;
import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.CellType;
import org.apache.poi.ss.usermodel.DateUtil;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.ss.usermodel.Sheet;
import org.apache.poi.ss.usermodel.Workbook;
import org.apache.poi.util.IOUtils;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;

import java.io.*;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * excel 文件读取类
 * 数据格式处理采用-策略模式
 * @Author: chengbo
 * @Date: 2018/10/12
 */
public class ExcelReader {

    private static final String[] EXCEL_EXTENSION = {".xlsx",".xls"};

    private Workbook workbook;
    private File file;
    private InputStream inputStream;
    //private List<DataHandleStrategy> dataHandles = new ArrayList<>();
	private List<DataCaseStrategy> dataCases = new ArrayList<>(8);
    private List<DataMergeStrategy> dataMerges = new ArrayList<>(8);
    private List<DataSplitStrategy> dataSplits = new ArrayList<>(8);
    // 待优化，build后会改变该值
    private boolean hasHead = false;

    /**
     * 创建excel解析对象
     * @param filePath
     * @throws IOException
     */
    public ExcelReader(String filePath) throws IOException {
        if(filePath == null){
            throw new NullPointerException("excel file is null !");
        }
        File file = new File(filePath);
        if(!file.exists()){
            throw new FileNotFoundException("excel file is not found !");
        }
        this.file = file;
        this.inputStream = new FileInputStream(file);
        String fileName = file.getName().toLowerCase();
        if(fileName.endsWith(EXCEL_EXTENSION[0])){
            this.workbook = new XSSFWorkbook(this.inputStream);
        }else if(fileName.endsWith(EXCEL_EXTENSION[1])){
            this.workbook = new HSSFWorkbook(this.inputStream);
        }else{
            throw new IOException("file type is not support !");
        }
    }

    /**
     * 添加数据转换处理策略
     * @param dataCase
     */
    public  void addDataCase(DataCaseStrategy dataCase){
        this.dataCases.add(dataCase);
    }

	/**
	 * 添加数据合拼处理策略
	 * @param dataMerge
	 */
	public void addDataMergeHandle(DataMergeStrategy dataMerge){
    	this.dataMerges.add(dataMerge);
	}

	public void addDataSplitHandle(DataSplitStrategy dataSplit){
		this.dataSplits.add(dataSplit);
	}

    /**
     * 关闭流连接
     */
    public void close(){
        IOUtils.closeQuietly(this.inputStream);
    }

    /**
     * 加载数据构建到bean中
     * @return
     */
    public ExcelBean build(){
        ExcelBean excelBean = new ExcelBean(this.file);        
        int sheetSize = workbook.getNumberOfSheets();
        for(int i = 0; i < sheetSize; i++ ){
            excelBean.addSheetBean(buildSheetBean(excelBean, i));
        }
        return excelBean;
    }
    
    /**
     * 加载excel构建到bean中,使用第一行做head
     * @return
     */
    public ExcelBean buildHasHead(){
    	this.hasHead = true;
    	return build();
    }
    
    /**
     * 加载页数据
     * @param excelBean
     * @param sheetIndex
     * @return
     */
	private ExcelBean.SheetBean buildSheetBean(ExcelBean excelBean, int sheetIndex) {
		ExcelBean.SheetBean sheetBean = excelBean.newSheetBean();
		Sheet sheet = workbook.getSheetAt(sheetIndex);
		sheetBean.setSheetName(sheet.getSheetName());		
		int lastRowNum = sheet.getLastRowNum();
		if(lastRowNum==0){
			return sheetBean;
		}
		int cellSize = 0;
		//加载头标题
		if(this.hasHead){
			List<String> heads = new ArrayList<String>();
			Row headRow = sheet.getRow(0);
			cellSize = headRow.getLastCellNum();
			for(int j=0; j < cellSize ; j++){
				heads.add(headRow.getCell(j).getStringCellValue());
			}
			sheetBean.setHeads(heads);
		}
		//加载内容数据
		List<String> heads = sheetBean.getHeads();
		for(int i = this.hasHead?1:0 ; i < lastRowNum; i++ ){
			Map<String, Object> rowVal = new HashMap<String, Object>();
			Row row = sheet.getRow(i);
			if(row == null){
				continue;
			}
			cellSize = heads==null?row.getLastCellNum():heads.size();
			for(int j=0; j < cellSize ; j++){
				Object value = getCellValue(row.getCell(j));
				value = dataCaseHandle(value);
				if(heads == null){
					rowVal.put(j+"", value);
				}else{
					rowVal.put(heads.get(j), value);
				}
			}
			dataMergeHandle(rowVal);
			dataSplitHandle(rowVal);
			sheetBean.addRow(rowVal);
		}
		return sheetBean;
	}

	/**
	 * split 数据处理
	 * @param rowVal
	 */
	private void dataSplitHandle(Map<String, Object> rowVal) {
		if(rowVal == null || this.dataSplits.size() == 0){
			return ;
		}
		for(DataSplitStrategy dataMerge : this.dataSplits){
			dataMerge.dataSplit(rowVal);
		}
	}

	/**
	 * merge 数据处理
	 * @param rowVal
	 */
	private void dataMergeHandle(Map<String, Object> rowVal) {
		if(rowVal == null || this.dataMerges.size() == 0){
			return ;
		}
		for(DataMergeStrategy dataMerge : this.dataMerges){
			dataMerge.dataMerge(rowVal);
		}
	}

	/**
	 * 数据格式转换
	 * @param value
	 * @return
	 */
	private Object dataCaseHandle(Object value){
		if(this.dataCases.size() == 0){
			return value;
		}
		for(DataCaseStrategy dataCase : this.dataCases){
			value = dataCase.dataCase(value);
		}
		return value;
	}

	/**
	 * 获取cell 数据值
	 * @param cell
	 * @return 不返回null, 空则返回""
	 */
	private Object getCellValue(Cell cell) {
		Object value = "";
		if(cell == null){
			return value;
		}
		CellType cellType = cell.getCellTypeEnum();	
		if(cellType == CellType.NUMERIC){
			if(DateUtil.isCellDateFormatted(cell)){
				value = cell.getDateCellValue();
			}else{
				value = cell.getNumericCellValue();
			}
		}else if(cellType == CellType.BOOLEAN){
			value = cell.getBooleanCellValue();
		}else if(cellType == CellType.STRING){
			value = cell.getStringCellValue();
		}else if(cellType == CellType._NONE || cellType == CellType.BLANK){
			value = "";
		}else{
			value = cell.getRichStringCellValue();
		}
		return value;
	}

}
