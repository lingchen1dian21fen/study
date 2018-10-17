package com.cbo.util.poi;

import java.io.IOException;

import org.apache.poi.ss.usermodel.CellType;

/**
 * @Author: chengbo
 * @Date: 2018/10/12
 */
public class POIUtil {
	
	public static void main(String[] args) throws IOException {
		ExcelReader reader = new ExcelReader("E:/chengbo/personal/phone-num/masage.xlsx");
		ExcelBean bean = reader.buildHasHead();
		System.out.println(bean);
	}
	
	
}
