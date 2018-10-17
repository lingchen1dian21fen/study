package com.cbo.data.handle;

/**
 * @Author: chengbo
 * @Date: 2018/10/17
 */
public interface DataCaseStrategy {

    /**
     * 数据类型，格式转换
     * @param value
     * @return
     */
    public Object dataCase(Object value);


}
