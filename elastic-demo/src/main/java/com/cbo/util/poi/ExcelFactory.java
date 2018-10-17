package com.cbo.util.poi;

import java.io.File;

/**
 * 
 * @author chengbo
 * @date 2018年10月12日 
 */
public class ExcelFactory {
	
	private ExcelFactory(){}
	
	public static ExcelFactory build(String filePath){
		if(filePath == null){
			throw new NullPointerException("filePath is null");
		}
		File file = new File(filePath);


		return null;
	}
	
	

}
