# -*-coding:utf-8 -*-
'''
Created on 2020-07-29 15:41

@author: chengbo

- 02 链表
            问题：实现单链表、循环链表、双向链表，支持增删操作
            问题：实现单链表反转
            问题：实现两个有序的链表连接为一个有序链表
            问题：实现求链表的中间结点

'''
class Node(object):
    """
                链表中的数据节点对象
    """
    
    def __init__(self, val, next_node=None, prev_node=None):
        self._data = val
        self._next = next_node
        self._prev = prev_node
    
    def __repr__(self):
        return str(self._data)


class OneWayLinked(object):
    """
                实现单链表，支持增删操作
    """
    
    def __init__(self):
        self._first = None
        self._len = 0 
        
    def __len__(self):
        return self._len
    
    def __item__(self):
        temp = self._first
        while temp:
            yield temp._data
            temp = temp._next
        return None    
    
    def __iter__(self):
        self._temp = self._first
        return self
    
    def __next__(self):
        if self._temp:
            val = self._temp._data
            self._temp = self._temp._next
            return val
        else:
            raise StopIteration
                 
    def append(self, val):
        self._len += 1
        if self._first == None:
            self._first = Node(val)
        else:
            temp = self._first
            while temp._next:
                temp = temp._next
            temp._next = Node(val)
            
    def peek(self):
        if self._len == 0:
            return None
        temp = self._first
        while temp._next:
            temp = temp._next
        return temp._data
    
    def get(self, index):
        if index < 0 or index > self._len:
            raise IndexError('linked index out of range! ')
        else:
            for i, val in enumerate(self):
                if index == i:
                    return val
        
        
    def pop(self):
        if self._len == 0:
            return None
        if self._len == 1:
            val = self._first._data
            self._first = None
            self._len = 0
            return val
        temp = self._first
        while True:
            if temp._next._next == None:
                val = temp._next._data
                temp._next = None
                self._len -= 1
                return val
            temp = temp._next

    def remove(self, val):
        if self._len == 0:
            return 
        if self._first._data == val:
            self._first = self._first._next
            self._len -= 1
            return 
        temp = self._first
        while temp._next:
            if temp._next._data == val:
                self._len -= 1
                n = temp._next._next
                temp._next = n
                return 
            else:
                temp = temp._next

    def rollback(self):
        '''
                              实现单链表反转
        '''       
        link = OneWayLinked()
        i = self._len
        while i > 0:
            i -= 1
            link.append(self.get(i))
        return link
    
    def joint(self, link):
        if len(link) == 0:
            return 
        for val in link:
            self.append(val)
            
    
    def reverse(self):        
        """
            优化单链表反转，时间为O(n)，空间为O(1)
        """
        pass
    
    def middle(self):
        if self._len == 0:
            return None
        if self._len % 2 == 0:
            return self.get(int(self._len/2) - 1)
        else:
            return self.get(int(self._len/2))

class TwoWayLinked(object):
    """
                实现双向链表，支持增删操作
    """
    def __init__(self):
        self._first = None
        self._last = None
        self._len = 0 
        
    def __len__(self):
        return self._len
    
    def __item__(self):
        temp = self._first
        while temp:
            yield temp._data
            temp = temp._next
        return None    
    
    def __iter__(self):
        self._temp = self._first
        return self
    
    def __next__(self):
        if self._temp:
            val = self._temp._data
            self._temp = self._temp._next
            return val
        else:
            raise StopIteration
                 
    def append(self, val):
        node = Node(val)
        if self._len == 0:
            self._first = node
            self._last = node
        else:
            node._prev = self._last
            self._last._next = node
            self._last = node
        self._len += 1
    
    def first(self):
        if self._len == 0:
            return None
        return self._first._data
    
    def last(self):
        if self._len == 0:
            return None
        return self._last._data
            
    def peek(self):
        if self._len == 0:
            return None       
        return self._last._data
    
    def get(self, index):
        if index < 0 or index > self._len:
            raise IndexError('linked index out of range! ')
        else:
            for i, val in enumerate(self):
                if index == i:
                    return val
                
    def pop(self):
        if self._len == 0:
            return None
        if self._len == 1:
            val = self._first._data
            self._first = None
            self._last = None
            self._len = 0
            return val
        val = self._last._data
        temp = self._last
        self._last = temp._prev
        self._last._next = None
        temp._prev = None
        self._len -= 1
        return val

    def remove(self, val):
        if self._len == 0:
            return
        if self._first._data == val:
            if self._len == 1:
                self._first = None
                self._last = None
                self._len = 0
                return
            else:
                self._first = self._first._next
                self._first._prev = None
                self._len -= 1
                return 
        temp = self._first
        while temp._next:
            if temp._next._data == val:
                self._len -= 1
                n = temp._next._next
                if self._last == temp._next:
                    self._last = temp
                temp._next._prev = None
                temp._next._next = None
                temp._next = n
                return 
            else:
                temp = temp._next           

    def joint(self, link):
        if len(link) == 0:
            return 
        for val in link:
            self.append(val)
            
    def middle(self):
        if self._len == 0:
            return None
        if self._len % 2 == 0:
            return self.get(int(self._len/2) - 1)
        else:
            return self.get(int(self._len/2))        

class CircularLinked(object):
    """
                实现循环链表，支持增删操作
    """
    
    def __init__(self):
        self._first = None
        self._last = None
        self._len = 0 
        
    def __len__(self):
        return self._len
    
    """
    def __item__(self):
        temp = self._first
        while temp:
            yield temp._data
            temp = temp._next
        return None    
    """
    
    def __iter__(self):
        self._temp = self._first
        return self
    
    def __next__(self):
        if self._temp:
            val = self._temp._data
            self._temp = self._temp._next
            return val
        else:
            raise StopIteration
    
    def get(self, index):
        if index < 0 :
            raise IndexError('linked index out of range! ')
        else:
            i = 0
            temp = self._first
            while temp:
                if i == index:
                    return temp._data
                else:
                    i += 1
                    temp = temp._next
                
                 
    def append(self, val):
        self._len += 1
        node = Node(val)
        if self._first == None:
            self._first = node
            self._last = node 
            self._last._next = self._first
        else:            
            self._last._next = node
            self._last = node
            self._last._next = self._first            

    def remove(self, val):
        if self._len == 0:
            return
        if self._first._data == val:
            if self._len == 1:
                self._first = None
                self._last = None
                self._len = 0
                return
            else:
                temp = self._first
                self._first = self._first._next
                self._last._next = self._first
                temp._next = None
                self._len -= 1
                return 
        temp = self._first
        while temp._next:
            if temp._next._data == val:
                self._len -= 1
                rnode = temp._next
                temp._next = rnode._next
                rnode._next = None
                if self._last == rnode:
                    self._last = temp
                    #self._last._next = self._first
                return 
            else:
                temp = temp._next    
                     
    def joint(self, link):
        if len(link) == 0:
            return 
        for val in link:
            self.append(val)
            
    def middle(self):
        if self._len == 0:
            return None
        if self._len % 2 == 0:
            return self.get(int(self._len/2) - 1)
        else:
            return self.get(int(self._len/2))        

def assert_one_way():
    l = OneWayLinked()
    l.append('aaa')
    l.append('bbb')
    l.append('ccc')
    assert len(l) == 3
    assert l.get(1) == 'bbb'
    for val in l:
        print(val)
    l.remove('bbb')
    assert len(l) == 2
    l.remove('ddd')
    assert len(l) == 2
    l.remove('aaa')
    l.remove('ccc')
    assert len(l) == 0
    print('单向链表断言结束！')

def assert_two_way():
    l = TwoWayLinked()
    l.append('aaa')
    assert l.first() == 'aaa'
    assert l.last() == 'aaa'
    
    l.append('bbb')
    l.append('ccc')
    assert len(l) == 3
    assert l.get(1) == 'bbb'
    assert l.first() == 'aaa'
    assert l.last() == 'ccc'
    
    for val in l:
        print(val)
        
    l.remove('bbb')
    assert len(l) == 2
    assert l.first() == 'aaa'
    assert l.last() == 'ccc'
    
    l.remove('ddd')
    assert len(l) == 2
    assert l.first() == 'aaa'
    assert l.last() == 'ccc'
    
    l.remove('aaa')
    assert l.first() == 'ccc'
    assert l.last() == 'ccc'
    
    l.remove('ccc')
    assert len(l) == 0
    assert l.first() == None
    assert l.last() == None
    print('双向链表断言结束！')
    
def assert_cirular_way():
    l = CircularLinked()
    l.append('aaa')
    l.append('bbb')
    l.append('ccc')
    assert len(l) == 3
    assert l.get(1) == 'bbb'
    assert l.get(5) == 'ccc'
    
    i = 0
    it = iter(l)
    while i < 10:
        print(next(it))
        i += 1
    
    l.remove('ccc')
    assert len(l) == 2
    print('remove ccc ')
    it = iter(l)
    while i < 20:
        print(next(it))
        i += 1
    print('append ccc and remove aaa')
    l.append('ccc')
    l.remove('aaa')
    it = iter(l)  
    while i < 30:
        print(next(it))
        i += 1
    print('循环链表断言结束！')
    
def assert_rollback():
    l = OneWayLinked()
    l.append('aaa')
    l.append('bbb')
    l.append('ccc')
    l.append('ddd')
    lr = l.rollback()
    assert lr.get(0) == 'ddd'
    assert lr.get(1) == 'ccc'
    assert lr.get(2) == 'bbb'
    assert lr.get(3) == 'aaa'
    for val in lr:
        print(val)
    print('单链表反转 断言结束！')
    
def assert_joint():
    l = OneWayLinked()
    l.append('aaa')
    l.append('bbb')
    l.append('ccc')
    l.append('ddd')
    
    l1 = OneWayLinked()
    l1.append('111')
    l1.append('222')
    l1.append('333')

    l2 = TwoWayLinked()
    l2.append('hhh')
    l2.append('tt')
    l2.append('234')
    
    l3 = CircularLinked()
    l3.append('ert')
    l3.append('hfgh')
    l3.append('qdfh')
    
    l1.joint(l)
    assert len(l1) == 7
    assert l1.get(4) == 'bbb'
    
    l2.joint(l)
    assert len(l2) == 7
    assert l2.get(4) == 'bbb'
    
    l3.joint(l)
    assert len(l3) == 7
    assert l3.get(4) == 'bbb'
    
    l.remove('aaa')
    assert len(l1) == 7
    assert len(l2) == 7
    assert len(l3) == 7
    
    print('链表拼接 断言结束！')   
    
def assert_middle():
    l1 = OneWayLinked()
    l1.append('111')
    assert l1.middle() == '111'

    l2 = TwoWayLinked()
    l2.append('hhh')
    l2.append('tt')
    l2.append('234')
    assert l2.middle() == 'tt'
    
    l3 = CircularLinked()
    l3.append('ert')
    l3.append('hfgh')
    l3.append('qdfh')    
    l3.append('222')
    assert l3.middle() == 'hfgh' 
    
    print('链表中间节点 断言结束！')      

if __name__ == '__main__':
    # 单链表 
    assert_one_way()
    # 双链表
    assert_two_way()
    # 循环链表
    assert_cirular_way()
    # 单链表反转
    assert_rollback()
    # 链表拼接
    assert_joint()
    # 链表中间节点
    assert_middle()
    
    