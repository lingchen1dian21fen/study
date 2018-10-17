package com.cbo.data.handle;

import java.util.Map;

/**
 * @Author: chengbo
 * @Date: 2018/10/17
 */
public interface DataSplitStrategy {

    public Map<String,Object> dataSplit(Map<String, Object> row);

}
