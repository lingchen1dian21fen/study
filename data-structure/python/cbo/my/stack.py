# -*-coding:utf-8 -*-
'''
Created on 2020-07-31 10:05

@author: chengbo

- 03 栈
            问题：用数组实现一个顺序栈
            问题：用链表实现一个链式栈
            问题：编程模拟实现一个浏览器的前进、后退功能

'''
from cbo.my.array import DynamicArray
from cbo.my.linked import TwoWayLinked

class SequenceStack(object):
    """
        顺序栈
    """
    def __init__(self):
        self._data = DynamicArray()
    
    def __len__(self):
        return len(self._data)
    
    def __item__(self):
        i = self.__len__() - 1
        while i >= 0:
            yield self._data[i]
            i -= 1
     
    def push(self, value):
        self._data[self.__len__()] = value
        
    def pop(self):    
        val = self._data[self._len - 1]
        self._data.delete(self._len - 1)
        return val
    
    def peek(self):
        return self._data[self._len - 1]

class LinkedStack(object):
    """
        链式栈
    """
    def __init__(self):
        self._data = TwoWayLinked()
    
    def __len__(self):
        return len(self._data)
    
    def __item__(self):
        pass
     
    def push(self, value):
        self._data.append(value)
        
    def pop(self):    
        return self._data.pop()
    
    def peek(self):
        return self._data.peek()

class Browser(object):
    """
    模拟浏览器对象，实现前进和后退功能
    """
    def __init__(self, url):
        self._history = SequenceStack()
        self._curr = url
        self._back = SequenceStack()

    def go_down(self):
        self._back.push(self._curr)
        self._curr = self._history.pop()
    
    def go_up(self):
        self._history.push(self._curr)
        self._curr = self._back.pop()

    def browse(self, url):
        self._history.push(self._curr)
        self._curr = url




if __name__ == '__main__':
    pass