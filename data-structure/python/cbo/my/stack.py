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
    
    def __iter__(self):
        for d in self._data:
            yield d
        return None
     
    def push(self, value):
        self._data[self.__len__()] = value
        
    def pop(self):  
        if self.__len__() == 0:
            return None  
        val = self._data[self.__len__() - 1]
        self._data.delete(self.__len__() - 1)
        return val
    
    def peek(self):
        if self.__len__() == 0:
            return None
        return self._data[self.__len__() - 1]

class LinkedStack(object):
    """
        链式栈
    """
    def __init__(self):
        self._data = TwoWayLinked()
    
    def __len__(self):
        return len(self._data)
    
    def __iter__(self):
        for d in self._data:
            yield d
        return None
     
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
        if len(self._history) == 0:
            return 
        self._back.push(self._curr)
        self._curr = self._history.pop()
        return self._curr
    
    def go_up(self):
        if len(self._back) == 0:
            return
        self._history.push(self._curr)
        self._curr = self._back.pop()
        return self._curr

    def browse(self, url):
        self._history.push(self._curr)
        self._curr = url
        return self._curr
        
    def get(self):
        return self._curr

def assert_sequence():
    stack = SequenceStack()
    stack.push('aaa')
    stack.push('bbb')
    stack.push('ccc')
    stack.push('ddd')
    assert len(stack) == 4
    assert stack.peek() == 'ddd'
    assert stack.pop() == 'ddd'
    assert stack.pop() == 'ccc'
    assert len(stack) ==2
    for data in stack:
        print(data)
    print('顺序栈 断言结束')
    
def assert_linked():
    stack = LinkedStack()   
    stack.push('aaa')
    stack.push('bbb')
    stack.push('ccc')
    stack.push('ddd')
    assert len(stack) == 4
    assert stack.peek() == 'ddd'
    assert stack.pop() == 'ddd'
    assert stack.pop() == 'ccc'
    assert len(stack) ==2
    for data in stack:
        print(data)
    print('链式栈 断言结束') 
    
def assert_browser():
    b = Browser('aaa')
    b.browse('bbb')
    b.browse('ccc')
    assert b.get() == 'ccc'
    assert b.go_up() == None
    assert b.go_down() == 'bbb'
    assert b.go_up() == 'ccc'
    b.go_down()
    b.go_down()
    assert b.get() == 'aaa'
    print('模拟浏览器 断言结束') 
    
if __name__ == '__main__':
    # 顺序栈
    assert_sequence()
    # 链式栈
    assert_linked()
    # 模拟浏览器
    assert_browser()
    