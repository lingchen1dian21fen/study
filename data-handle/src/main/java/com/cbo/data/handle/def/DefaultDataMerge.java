package com.cbo.data.handle.def;

import com.cbo.data.handle.DataMergeStrategy;

import java.util.List;
import java.util.Map;

/**
 * @Author: chengbo
 * @Date: 2018/10/17
 */
public class DefaultDataMerge implements DataMergeStrategy {

    /**
     * 合并分隔符
     */
    private String reg;

    /**
     * 需要合并的keys及合并后的key
     * 使用List<String> 可以保证顺序，但是不能保证唯一
     */
    private Map<String,List<String>> mergeKeys;
    /**
     * 是否代替原keys，如果未true，代替原有keys，则新的keys中移除被合并的key-value,只保留新加的key
     * 默认为true
     */
    private boolean replace = true;

    public DefaultDataMerge(Map<String,List<String>> mergeKeys,String reg){
        this.mergeKeys = mergeKeys;
        this.reg = reg;
    }

    public DefaultDataMerge(Map<String,List<String>> mergeKeys){
        this.mergeKeys = mergeKeys;
        this.reg = "";
    }

    @Override
    public Map<String, Object> dataMerge(Map<String, Object> row) {
        if(row == null || this.mergeKeys == null || this.mergeKeys.size() == 0){
            return row;
        }
        for(String newKey : this.mergeKeys.keySet()){
            StringBuffer buff = new StringBuffer();
            for(String key : this.mergeKeys.get(newKey)){
                Object val = row.get(key);
                if(val != null){
                    buff.append(val);
                    buff.append(reg);
                    if(this.replace){
                        row.remove(key);
                    }
                }
            }
            String newValue = buff.length() == 0 ? "" : buff.substring(0,buff.length() - reg.length());
            row.put(newKey,newValue);
        }
        return row;
    }

    public Map<String, List<String>> getMergeKeys() {
        return this.mergeKeys;
    }
}
