# -*-coding:utf-8 -*-
'''
Created on 2020-08-13 19:10

@author: chengbo

- 08 散列表
            问题：实现一个基于链表法解决冲突问题的散列表
            问题：实现一个LRU缓存淘汰算法
'''
class HashTable(object):
    
    class Node(object):

        def __init__(self, key, val, next=None):  # @ReservedAssignment
            self._key = key
            self._val = val
            self._next = next
        
        def __repr__(self):
            return str((self._key, self._val))
    
    class Linked(object):
        
        def __init__(self):
            self._first = None
            self._len = 0 
        
        def __len__(self):
            return self._len   
        
        def add(self, key, value):
            node = HashTable.Node(key, value)
            if self._len == 0:
                self._first = node
                self._len += 1
                return 1
            else:
                temp = self._first
                while temp:
                    if temp._key == key:
                        temp._val = value
                        break
                    else:
                        temp = temp._next
                if not temp:
                    node._next = self._first
                    self._first = node
                    self._len += 1
                    return 1
                return 0
            
            
        def get(self, key, default=None):        
            if self._len != 0:
                temp = self._first
                while temp:
                    if temp._key == key:
                        return temp._val
                    else:
                        temp = temp._next 
            return default      
              
        def remove(self, key):
            if self._len == 0:
                return 0
            if self._first._key == key:
                self._first = self._first._next
                self._len -= 1
                return 1
            temp = self._first
            while temp._next:
                if temp._next._key == key:
                    self._len -= 1
                    n = temp._next._next
                    temp._next = n
                    return 1
                else:
                    temp = temp._next
            return 0        
                    
    _load_factor = 0.8   

    def __init__(self, size=16):
        self._table = [None] * size       
        self._len = 0
    
    def __len__(self):
        return self._len
    
    def _hash(self, key):
        return abs(hash(key)) % len(self._table)
    
    def put(self, key, value):
        index = self._hash(key)
        link = self._table[index]
        if link:
            n = link.add(key, value)
            self._len += n
        else:
            link = self.Linked()
            link.add(key, value)
            self._table[index] = link
            self._len += 1
                    
    
    def get(self, key, default=None):
        index = self._hash(key)
        link = self._table[index]
        if link:
            return link.get(key, default)
        else:
            return default
    
    def remove(self, key):
        index = self._hash(key)
        link = self._table[index]
        if link:
            n = link.remove(key)
            self._len -= n    

        
if __name__ == '__main__':
    table = HashTable(3)
    table.put(1, 'aaa')
    table.put('2', 'bbb')
    table.put('3', 'ccc')
    table.put(4, 'vvv')
    assert len(table) == 4
    assert table.get('2') == 'bbb'
    assert table.get(4) == 'vvv'
    table.remove('a')
    assert len(table) == 4
    table.put(1,'xxx')
    assert len(table) == 4
    table.remove('2')
    assert len(table) == 3
    print('断言结束')
    
    