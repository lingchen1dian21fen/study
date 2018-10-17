package com.cbo.data.handle.ext;

import com.cbo.data.handle.DataCaseStrategy;

/**
 * @Author: chengbo
 * @Date: 2018/10/17
 */
public class DataCaseNotNull implements DataCaseStrategy {
    @Override
    public Object dataCase(Object value) {
        if(value == null){
            return "";
        }
        return value;
    }
}
