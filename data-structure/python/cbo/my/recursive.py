# -*-coding:utf-8 -*-
'''
Created on 2020-08-06 14:28

@author: chengbo

- 05 递归
            问题：编程实现斐波那契数列求值f(n)=f(n-1)+f(n-2)
            问题：编程实现求阶乘n!
            问题：编程实现一组数据集合的全排列    

'''
from test.test_audioop import datas

def fibonacci(n):
    assert n >= 1
    if n < 3:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def factorial(n):
    assert n >= 0
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)


def permutation(datas, s, e, result):
    if s == e:
        result.append(list(datas))
    else:
        for i in range(s,e):
            datas[i], datas[s] = datas[s], datas[i]
            permutation(datas, s + 1, e, result)
            datas[i], datas[s] = datas[s], datas[i]

def assert_fibo():
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13
    assert fibonacci(8) == 21
    print('实现斐波那契数列 断言结束')


def assert_fact():
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(4) == 24
    assert factorial(5) == 120
    assert factorial(6) == 720
    print('实现求阶乘  断言结束')


def assert_perm():
    res = []
    datas = ['a', 'b', 'c']
    permutation(datas, 0, len(datas), res)
    assert len(res) == 6
    for r in res:
        print(r)
    print('-------------')   
    res = []
    datas = ['A', 'B', 'C', 'D']
    permutation(datas, 0, len(datas), res)
    assert len(res) == 24
    for r in res:
        print(r)         
    print('全排列 断言结束')

if __name__ == '__main__':
    # 实现斐波那契数列
    assert_fibo()
    # 实现求阶乘
    assert_fact()
    # 全排列  
    assert_perm()