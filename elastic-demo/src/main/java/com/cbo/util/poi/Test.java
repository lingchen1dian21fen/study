package com.cbo.util.poi;

import java.util.Date;
import java.util.HashMap;
import java.util.Map;

/**
 * @Author: chengbo
 * @Date: 2018/10/17
 */
public class Test {

    public static void main(String[] args) {
        Map<String,Object> map = new HashMap<>(16);
        map.put("aaa",new Date());
        map.put("bbb","ddd");
        map.put("ccc",Double.MIN_VALUE);
        map.put("ddd",new String[]{"1","2","3"});
        System.out.println(map.get("aaa"));
        System.out.println(map.get("bbb"));
        System.out.println(map.get("ccc"));
        System.out.println(map.get("ddd"));
    }


}
