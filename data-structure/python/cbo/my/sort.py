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

def quick_sort(datas, l, r):
    if l < r:
        i, j = l, r
        x = datas[i]
        while i < j:
            while i < j:
                if datas[j] < x:
                    datas[i] = datas[j]
                    i += 1
                    break
                j -= 1
            while i < j:        
                if datas[i] > x:
                    datas[j] = datas[i]
                    j -= 1
                    break
                i += 1
        datas[i] = x
        quick_sort(datas, l, i - 1)
        quick_sort(datas, i + 1, r)

def find_k_val(datas, l, r, k):
    if l < r:
        i, j = l, r
        x = datas[i]
        while i < j:
            while i < j:
                if datas[j] > x:
                    datas[i] = datas[j]
                    i += 1
                    break
                j -= 1
            while i < j:        
                if datas[i] < x:
                    datas[j] = datas[i]
                    j -= 1
                    break
                i += 1
        datas[i] = x
        if i + 1 == k:
            return datas[i]
        elif i + 1 > k:
            return find_k_val(datas, l, i - 1, k)
        else:
            return find_k_val(datas, i + 1, r, k)

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
    
def assert_quick():
    datas = [3, 5, 1, 8, 2, 4, 9, 6, 7]
    quick_sort(datas, 0, len(datas) - 1)
    assert datas[0] == 1
    assert datas[4] == 5
    assert datas[8] == 9
    print(datas)
    print('快速排序  测试结束')
    
def assert_k_val():
    datas = [3, 5, 1, 8, 2, 4, 9, 6, 7]
    assert find_k_val(datas, 0, len(datas)-1, 3) == 7
    assert find_k_val(datas, 0, len(datas)-1, 8) == 2
    print('第K大值  测试结束')    

if __name__ == '__main__':
    assert_bubble()
    assert_selection()
    assert_merge()
    assert_insert()
    assert_quick()
    assert_k_val()
    
    