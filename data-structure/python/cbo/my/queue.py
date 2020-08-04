# -*-coding:utf-8 -*-
'''
Created on 2020-08-03 19:13

@author: chengbo

- 04 队列
            问题：用数组实现一个顺序队列
            问题：用链表实现一个链式队列
            问题：实现一个循环队列

'''
from cbo.my.array import DynamicArray
from cbo.my.linked import TwoWayLinked

class SequenceQueue(object):
    
    def __init__(self):
        self._data = DynamicArray()
        
    def __len__(self):
        return len(self._data)

    def __iter__(self):
        for data in self._data:
            yield data
        return None
    
    def push(self, value):
        self._data[self.__len__()] = value

    def pop(self):
        if self.__len__() == 0:
            return None    
        val = self._data[0]
        self._data.delete(0)
        return val
    
    def peek(self):
        if self.__len__() == 0:
            return None
        return self._data[0]

class LinkedQueue(object):
    
    def __init__(self):
        self._data = TwoWayLinked()
        
    def __len__(self):
        return len(self._data)

    def __iter__(self):
        for data in self._data:
            yield data
        return None
    
    def push(self, value):
        self._data.append(value)

    def pop(self):
        if self.__len__() == 0:
            return None    
        return self._data.pop_first()
    
    def peek(self):
        if self.__len__() == 0:
            return None
        return self._data.first()
    
    
def assert_sequence():
    queue = SequenceQueue()
    queue.push('aaa')
    queue.push('bbb')
    queue.push('ccc')
    queue.push('ddd')
    assert len(queue) == 4
    assert queue.peek() == 'aaa'
    assert queue.pop() == 'aaa'
    assert queue.pop() == 'bbb'
    assert len(queue) == 2
    for data in queue:
        print(data)
    print('顺序队列 断言结束')

def assert_lined():
    queue = LinkedQueue()
    queue.push('aaa')
    queue.push('bbb')
    queue.push('ccc')
    queue.push('ddd')
    assert len(queue) == 4
    assert queue.peek() == 'aaa'
    assert queue.pop() == 'aaa'
    assert queue.pop() == 'bbb'
    assert len(queue) == 2
    for data in queue:
        print(data)
    print('链表队列 断言结束')

if __name__ == '__main__':
    # 顺序队列
    assert_sequence()
    # 链表队列 
    assert_lined()