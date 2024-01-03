#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

if __name__ == '__main__':

    A=list(map(float,input('enter list elems: ').split()))
    a=int(input('enter value a: '))
    b = int(input('enter value b: '))
    print(f"max value-{max(A)}")
    l=0
    for i,item in enumerate(A):
        if item>0:
            l=i

    s=sum(A[:l+1])
    print(f'sum elems until last positive elem: {s}')
    d=[i for i in A if abs(i)>a and abs(i)<b]
    print(f'redacted list: {d}')
    la=len(A)
    ld=len(d)
    while ld!=la:
        d.append(0)
        ld=len(d)
    print(f'list with nulls: {d}')




