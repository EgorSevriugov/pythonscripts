# -*- coding: utf8 -*-
from random import random

A = [1,2,3,4,5]
A[::2],A[1::2] = A[:len(A)//2+len(A)%2:],A[-1:len(A)//2*(-1) - 1:-1]
print(A)