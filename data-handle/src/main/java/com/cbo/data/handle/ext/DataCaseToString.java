package com.cbo.data.handle.ext;

import com.cbo.data.handle.DataCaseStrategy;

/**
 * @Author: chengbo
 * @Date: 2018/10/17
 */
public class DataCaseToString implements DataCaseStrategy {
    @Override
    public Object dataCase(Object value) {
        return String.valueOf(value);
    }
}
