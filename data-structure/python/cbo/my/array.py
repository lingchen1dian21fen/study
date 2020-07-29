# -*-coding:utf-8 -*-
'''
Created on 2020-07-28 15:34

@author: chengbo

    - 01 数组
            问题：实现一个支持动态扩容的数组
            问题：实现一个大小固定的有序数组，支持动态增删改操作
            问题：实现两个有序数组合并为一个有序数组

'''


class Array1(object):
    """
                支持动态扩容的数组，数组：可以通过下标操作数据，有长度，可以遍历
    """  
    
    def __init__(self, *data):
        self._data = list(data)        
        
    def __getitem__(self, index):
        return self._data[index]
    
    def __setitem__(self, index, value):
        if index < len(self._data) and index >= 0:
            self._data[index] = value
        else:
            i = len(self._data)
            while i < index:
                i += 1
                self._data.append(None)
            self._data.append(value)
    
    def __len__(self):
        return len(self._data)

    def __item__(self):
        for item in self._data:
            yield item
    
    def get_datas(self):
        return self._data
    
    # 实现两个有序数组合并为一个有序数组
    def merge(self, array):
        d = self.get_datas() if len(self) >= len(array) else array.get_datas()
        res = Array1(*d)
        s = len(self._data) if len(self._data) <= len(array) else len(array)
        i = 0
        while i < s:
            res[i] = self._data[i] if array[i] == None else array[i]
            i += 1
        return res    
    
    
class Array2(object):
    """
                实现一个大小固定的有序数组，支持动态增删改操作
    """
    def __init__(self, capacity=-1, *data):
        self._data = list(data)        
        if len(data) > capacity:
            self._capacity = len(data)
        else:
            self._capacity = capacity
            while len(self._data) < self._capacity :
                self._data.append(None)

    def __len__(self):
        return self._capacity

    def __getitem__(self, index):
        if index >= 0 and index < self._capacity:
            return self._data[index]
        else:
            raise IndexError('array index out of range!')     
                
    def __setitem__(self, index, value):
        if index >= 0 and index < self._capacity:         
            self._data.insert(index, value)
        else:
            raise IndexError('array index out of range!')

    def __item__(self):
        for item in self._data:
            yield item

    def insert(self, index, value):
        self.__setitem__(index, value)
        
    def update(self, index, value):
        self.__setitem__(index, value)
    
    def delete(self, index):
        if index >= 0 and index < self._capacity:
            self._data[index] = None
        else:
            raise IndexError('array index out of range!')


def assert_array1():    
    a1 = Array1()
    assert len(a1) == 0
    a1[2] = 1
    assert len(a1) == 3    
    a1[3] = 'aaa'
    assert len(a1) == 4
    for a in a1:
        print(a)
    a2 = Array1('aa', 'bb', 'cc')
    for a in a2:
        print(a)
    print('支持动态扩容的数组 断言结束！')    

def assert_array2():
    a2 = Array2(5)
    assert len(a2) == 5
    assert a2[4] == None
    a2[4] = 5
    assert len(a2) == 5
    assert a2[4] == 5
    a2.insert(2,'aaa')
    assert a2[2] == 'aaa'
    a2.update(2,'bbb')
    assert a2[2] == 'bbb'
    assert len(a2) == 5
    a2.delete(2)
    assert a2[2] == None
    assert len(a2) == 5
    try:
        a2[6] = 6
    except IndexError:
        assert True
    else:
        assert False
    try:
        a2.insert(6,'aaa')
    except IndexError:
        assert True
    else:
        assert False
    a1 = Array2(4, 'aaa', 'bbb', 'ccc')
    for a in a1:
        print(a)  
    print('大小固定的有序数组 断言结束！')  

def assert_array3():
    a1 = Array1()
    a1[0] = 'aaa'
    a1[1] = 'bbb'
    a1[2] = 'ccc'
    a2 = Array1()
    a2[1] = 'bbb'
    a2[2] = '444'
    a2[5] = 'ccc'
    a3 = a1.merge(a2)
    # 合并不影响原数组
    assert a1[2] == 'ccc'
    assert a2[0] == None
    #    
    assert a3[0] == 'aaa'
    assert a3[1] == 'bbb'
    assert a3[2] == '444'
    assert a3[3] == None
    assert a3[5] == 'ccc'
    assert len(a3) == 6
    print('两个有序数组合并 断言结束！')  

if __name__ == '__main__':
    # 支持动态扩容的数组
    assert_array1()
    # 大小固定的有序数组
    assert_array2()
    # 实现两个有序数组合并为一个有序数组    
    assert_array3()
    #a = []
    #a[2] = 'aaa'
    #print(a[0])


