package com.cbo.data.handle.def;

import com.cbo.data.handle.DataSplitStrategy;

import java.util.Map;
import java.util.Set;

/**
 * @Author: chengbo
 * @Date: 2018/10/17
 */
public class DefaultDataSplit implements DataSplitStrategy {

    /**
     * 切割的正则表达式
     */
    private String reg;
    /**
     * 需要切割的key
     */
    private Set<String> splitKeys;
    /**
     * 是否代替原keys，如果未true，为代替原有keys，则新的keys中移除被合并的key-value,只保留新加的key
     * 默认为true
     */
    private boolean replace;

    public DefaultDataSplit(Set<String> splitKeys,String reg){
        this.splitKeys = splitKeys;
        this.reg = reg;
    }

    @Override
    public Map<String, Object> dataSplit(Map<String, Object> row) {
        if(row == null || this.splitKeys == null || this.splitKeys.size() == 0){
            return row;
        }
        for(String key : this.splitKeys){
            Object value = row.get(key);
            if(value != null){
                String val = String.valueOf(value);
                row.put(key,val.split(this.reg));
            }
        }
        return row;
    }


}
