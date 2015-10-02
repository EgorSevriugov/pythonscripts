# -*- coding: utf8 -*-
inp = open("int_data.txt")
file = str(inp.read())
file = file[:-1]
counts = []
ch = list(map(int,file.split(" ")))
for i in range(max(ch)+1):
    counts.append(ch.count(ch[i]))
    print('Колличество ',i,'равно:',ch.count(ch[i]))
print ('Самое часто встречающееся:',counts.index(max(counts)))
print ('Самое часто редковстречающееся:',counts.index(min(counts)))
print ('Различных чисел:',(101-counts.count(0)))