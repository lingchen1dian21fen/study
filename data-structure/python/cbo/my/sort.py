# -*-coding:utf-8 -*-
'''
Created on 2020-08-07 15:08

@author: chengbo

- 06 排序
            问题：冒泡排序
            问题：归并排序
            问题：快速排序
            问题：插入排序       
            问题：选择排序
            问题：编程实现O(n)时间复杂度内找到一组数据的第K大元素    

'''
from math import floor

def bubble_sort(datas):
    for i in range(len(datas) - 1):
        for j in range(i + 1, len(datas)):
            if datas[i] > datas[j]:
                datas[i], datas[j] = datas[j], datas[i]
    return datas        
            
def selection_sort(datas):
    for i in range(len(datas) - 1):
        min_index = i  
        for j in range(i + 1, len(datas)):
            if  datas[min_index] > datas[j]:
                min_index = j
        if min_index != i:
            datas[i], datas[min_index] = datas[min_index], datas[i]
    return datas        

def merge_sort(datas):
    if len(datas) < 2:
        return datas
    middle = floor(len(datas) / 2)
    left = datas[:middle:]
    rigth = datas[middle::]
    return _merge(merge_sort(left), merge_sort(rigth))

def _merge(left, right):
    res = []
    while left and right:
        if left[0] <= right[0]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))
    while left:
        res.append(left.pop(0)) 
    while right:
        res.append(right.pop(0))
    return res

def insert_sort(datas):
    if len(datas) < 2:
        return 
    i = 1
    while i < len(datas):
        j = i
        while j > 0:
            if datas[j] >= datas[j - 1]:
                break
            else:
                datas[j], datas[j - 1] = datas[j - 1], datas[j]
                j -= 1            
        i += 1

def quick_sort(datas):
    pass


def assert_bubble():
    datas = [3, 5, 1, 8, 2, 4, 9, 6, 7]
    bubble_sort(datas)
    assert datas[0] == 1
    assert datas[4] == 5
    assert datas[8] == 9
    print(datas)
    print('冒泡排序  测试结束')

def assert_selection():
    datas = [3, 5, 1, 8, 2, 4, 9, 6, 7]
    selection_sort(datas)
    assert datas[0] == 1
    assert datas[4] == 5
    assert datas[8] == 9
    print(datas)
    print('选择排序  测试结束')
    
def assert_merge():
    datas = [3, 5, 1, 8, 2, 4, 9, 6, 7]
    res = merge_sort(datas)
    assert res[0] == 1
    assert res[4] == 5
    assert res[8] == 9
    print(res)
    print('归并排序  测试结束')    

def assert_insert():
    datas = [3, 5, 1, 8, 2, 4, 9, 6, 7]
    insert_sort(datas)
    assert datas[0] == 1
    assert datas[4] == 5
    assert datas[8] == 9
    print(datas)
    print('插入排序  测试结束')

if __name__ == '__main__':
    assert_bubble()
    assert_selection()
    assert_merge()
    assert_insert()
    