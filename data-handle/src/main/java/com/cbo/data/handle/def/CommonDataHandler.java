package com.cbo.data.handle.def;

import com.cbo.data.handle.DataCaseStrategy;
import com.cbo.data.handle.DataMergeStrategy;
import com.cbo.data.handle.DataSplitStrategy;

import java.util.Map;

/**
 * @Author: chengbo
 * @Date: 2018/10/17
 */
public class CommonDataHandler implements DataCaseStrategy,DataMergeStrategy,DataSplitStrategy {

    private DefaultDataHandler defaultDataHandler;


    @Override
    public Object dataCase(Object value) {
        return defaultDataHandler.dataCase(value);
    }

    @Override
    public Map<String, Object> dataMerge(Map<String, Object> row) {
        return defaultDataHandler.dataMerge(row);
    }

    @Override
    public Map<String, Object> dataSplit(Map<String, Object> row) {
        return defaultDataHandler.dataSplit(row);
    }
}
