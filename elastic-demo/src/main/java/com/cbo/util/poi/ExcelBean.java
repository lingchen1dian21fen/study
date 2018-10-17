package com.cbo.util.poi;

import java.io.File;
import java.io.Serializable;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.UUID;

/**
 * @Author: chengbo
 * @Date: 2018/10/12
 */
public class ExcelBean implements Serializable {

    /**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	
	private String uid;
	private String fileName;
	//private String filePath;
	private File file;
	private List<SheetBean> sheetBeans = new ArrayList<>();

	public ExcelBean(File file) {
		this.uid = UUID.randomUUID().toString();
		this.fileName = file.getName();
		this.file = file;
	}

	public void addSheetBean(SheetBean sheetBean){
		this.sheetBeans.add(sheetBean);
	}

	public ExcelBean() {
		this.uid = UUID.randomUUID().toString();
	}

	public String getUid() {
		return uid;
	}

	public void setUid(String uid) {
		this.uid = uid;
	}

	public String getFileName() {
		return fileName;
	}

	public void setFileName(String fileName) {
		this.fileName = fileName;
	}

	public File getFile() {
		return file;
	}

	public void setFile(File file) {
		this.file = file;
	}

	public List<SheetBean> getSheetBeans() {
		return sheetBeans;
	}

	public void setSheetBeans(List<SheetBean> sheetBeans) {
		this.sheetBeans = sheetBeans;
	}

	public SheetBean newSheetBean() {
		return new SheetBean(this.uid);
	}

	public class SheetBean implements Serializable{

		private String excelUid;
		private String sheetName;
		private List<String> heads;
		private List<Map<String,Object>> rows = new ArrayList<Map<String,Object>>();

		public SheetBean(String excelUid) {
			this.excelUid = excelUid;
		}

		public String getExcelUid() {
			return excelUid;
		}

		public void setExcelUid(String excelUid) {
			this.excelUid = excelUid;
		}

		public String getSheetName() {
			return sheetName;
		}

		public void setSheetName(String sheetName) {
			this.sheetName = sheetName;
		}

		public List<String> getHeads() {
			return heads;
		}

		public void setHeads(List<String> heads) {
			this.heads = heads;
		}

		public List<Map<String, Object>> getRows() {
			return rows;
		}

		public void setRows(List<Map<String, Object>> rows) {
			this.rows = rows;
		}

		public void addRow(Map<String, Object> rowVal) {
			this.rows.add(rowVal);
		}
	}


}
