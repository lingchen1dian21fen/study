package com.cbo.data.handle.def;

import com.cbo.data.handle.DataCaseStrategy;
import com.cbo.data.handle.DataMergeStrategy;
import com.cbo.data.handle.DataSplitStrategy;

import java.util.Map;

/**
 * @Author: chengbo
 * @Date: 2018/10/17
 */
public class DefaultDataHandler implements DataCaseStrategy, DataMergeStrategy,DataSplitStrategy {

    @Override
    public Object dataCase(Object value) {
        if(value instanceof String){
            return ((String) value).trim();
        }
        return value;
    }

    @Override
    public Map<String, Object> dataMerge(Map<String, Object> row) {
        return row;
    }

    @Override
    public Map<String, Object> dataSplit(Map<String, Object> row) {
        return row;
    }
}
