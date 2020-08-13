# -*-coding:utf-8 -*-
'''
Created on 2020-08-12 15:58

@author: chengbo

- 07 二分查找
            问题：实现一个有序数组的二分查找算法
            问题：实现模糊二分查找算法（比如大于等于给定值的第一个元素）

'''
from math import floor

def dichotomy(datas, val):
    left, right = 0, (len(datas) - 1)
    while left <= right:
        m = left + floor((right - left) / 2)
        if datas[m] == val:
            return m
        elif datas[m] > val:
            right = m - 1
        else :
            left = m + 1
    return -1 

def fuzzy_dichotomy(datas, val):
    left, right = 0, (len(datas) - 1)
    while left <= right:
        m = left + floor((right - left) / 2)
        if datas[m] >= val:
            if m - 1 < left or datas[m - 1] < val:
                return m
            right = m - 1
        else :
            left = m + 1
    return -1 
     
        
def assert_dichotomy():
    datas = [21, 22, 23, 24, 25, 26, 27, 28, 29]
    assert dichotomy(datas, 21) == 0
    assert dichotomy(datas, 24) == 3
    assert dichotomy(datas, 25) == 4
    assert dichotomy(datas, 29) == 8
    assert dichotomy(datas, 5) == -1
    datas = [21, 22, 23, 24, 25, 26, 27, 28]
    assert dichotomy(datas, 21) == 0
    assert dichotomy(datas, 24) == 3
    assert dichotomy(datas, 25) == 4
    assert dichotomy(datas, 28) == 7
    print('二分法查找 断言结束')
    
def assert_fuzzy():    
    datas = [3, 7, 15, 36, 57, 57, 89, 93, 98]
    assert fuzzy_dichotomy(datas, 15) == 2
    assert fuzzy_dichotomy(datas, 57) == 4
    assert fuzzy_dichotomy(datas, 50) == 4
    assert fuzzy_dichotomy(datas, 90) == 7
    assert fuzzy_dichotomy(datas, 10) == 2
    assert fuzzy_dichotomy(datas, 1) == 0
    assert fuzzy_dichotomy(datas, 100) == -1
    print('模糊二分法查找 断言结束')

if __name__ == '__main__':
    assert_dichotomy()
    assert_fuzzy()