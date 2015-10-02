# -*- coding: utf8 -*-
from random import random

inp = str(input())
ch = list(map(int,inp.split(" ")))
sec = int(input())
for i in range(sec):
    ch.insert(len(ch)-1-ch[len(ch)- 1],ch[len(ch)-1])
    ch.reverse()
    ch.remove(ch[0])
    ch.reverse()
print(ch)