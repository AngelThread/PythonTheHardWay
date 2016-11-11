#!/bin/python

import sys


n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)

right = a[0][0] + a[1][1] + a[2][2]
left =  a[0][2] + a[1][1] + a[2][0]

print abs(right - left )