package com.cbo.demo.sort;

import java.util.Arrays;

/**
 * @Author: chengbo
 * @Date: 2018/10/31
 */
public class CountSort {
    /**
     * 数组中有20个随机数，取值范围从0到10，要求用最快的速度把这20个数从小到大进行排序
     */


    /**
     * 计数排序
     * @param arr
     */
    public static int[] countSort(int[] arr){
        //参数校验
        if(arr.length<2){
            return arr;
        }
        //跨度计算
        int min = arr[0];
        int max = arr[0];
        for (int i = 0; i < arr.length; i++) {
            if(arr[i] > max){
                max = arr[i];
            }
            if (arr[i] < min){
                min = arr[i];
            }
        }
        //计数填充
        int d = max - min;
        int[] countArr = new int[d+1];
        for (int i = 0; i < countArr.length; i++) {
            countArr[i] = 0;
        }
        //计数
        for (int i = 0; i < arr.length; i++) {
            countArr[arr[i]-min]++;
        }
        //变数
        int sum = 0;
        for (int i = 0; i < countArr.length; i++) {
            sum += countArr[i];
            countArr[i] = sum;
        }
        //返回
        int[] sortArr = new int[arr.length];
        for (int i = arr.length - 1; i >= 0; i--) {
            sortArr[countArr[arr[i]-min] - 1] = arr[i];
            countArr[arr[i]-min]--;
        }
        return  sortArr;
    }




    public static void main(String[] args) {
        int[] arr = {95,97,92,97,94,99,93,99,95};
        int[] sort = countSort(arr);
        System.out.println(Arrays.toString(sort));
    }





}
