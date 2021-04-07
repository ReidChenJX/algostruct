#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @time     : 2021/4/6 14:47
# @Author   : ReidChen
# Document  ：树数据结构，包含树结构，二叉树，BP树等

from functools import reduce


def calc(*number):
    # 可变参数
    sum = 0
    for n in number:
        sum += n * n
    print(sum)


def person(name, age, **kw):
    # 关键字参数
    print('name:', name, 'age:', age, 'other:', kw)


def person_2(name, age, *, Love, girl):
    # 命名关键字参数
    print(name, age, Love, girl)
    pass


calc(1, 2, 3, 4, 5, 6, 7)
person('ReidChen', 26, Love='YaZi')
person_2('ReidChen', 26, Love='YaZi', girl='yaya')


def fn(x, y):
    return x * 10 + y


print(reduce(fn, [1, 3, 5, 7, 9]))


def is_odd(n):
    return n % 2 == 1


print(list(filter(is_odd, [1, 2, 3, 4, 5, 6, 8, 9])))


def not_empty(s):
    return s and s.strip()


print(list(filter(not_empty, ['A', '', 'B', None, 'C'])))

print('************分割*************')

'''查找范围内的素数'''


def _odd_iter():
    n = 1
    while True:
        n += 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)


for n in primes():
    if n < 1000:
        print(n)
    else:
        break
        
        
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax += n
        
        return ax
    return sum


def func():
    funcs = []
    for i in range(4):
        def f():
            return i*i
        
        funcs.append(f)
    return funcs


import functools
int2 = functools.partial(int, base=2)


class Fib(object):
    def __init__(self):
        self.a = 0
        self.b = 1
        
    def __iter__(self):
        return self
    
    def __next__(self):
        self.a, self.b = self.b, self.a+self.b
        if self.a > 100:
            raise StopIteration
        return self.a
    
    def __getitem__(self, item):
        a,b = 1,1
        for x in range(item):
            a, b = b, a+b
        return a