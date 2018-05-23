#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 14 Assignment"""


def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def compareTo(s1, s2):
    if len(s1) == len(s2):
        return int(0)
    elif len(s1) > len(s2):
        return int(1)
    elif len(s1) < len(s2):
        return int(-1)


if __name__ == '__main__':
    print(fibonacci(5))
    print(gcd(2, 3)
    print(compareTo('sunny', 'cloudy'))
