package com.cbo.data.handle;

import java.util.Map;

/**
 * @Author: chengbo
 * @Date: 2018/10/17
 */
public interface DataMergeStrategy {

    /**
     * 数据合并处理
     * @param row
     * @return
     */
    public Map<String,Object> dataMerge(Map<String, Object> row);


}
