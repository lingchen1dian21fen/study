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
    pass

def insert_sort(datas):
    pass

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

if __name__ == '__main__':
    assert_bubble()
    assert_selection()
    