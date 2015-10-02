# -*- coding: utf8 -*-
inp = open("float_data.txt","r")
ch = []
sum = 0
sumkv = 0
maxx = None
minn = None
lmaxx = maxx
lminn = minn
nummax = 0
nummin = 0
s1 = str('Среднее:')
s2 = str('Среднеквадратическое:')
s3 = str('Максимум:')
s4 = str('Положение максимума:')
s5 = str('Минимум:')
s6 = str('Положение минимума:')
file = str(inp.read())
file = file[:-1]
ch = list(map(float,(file.split(' '))))
for i in range(len(ch)):
    sum += ch[i]
    if maxx == None:
        maxx = ch[i]
        minn = ch[i]
    else:
        maxx = max(ch[i],maxx)
        minn = min(ch[i],minn)
srednee = sum / len(ch)
for i in range(len(ch)):
    sumkv += (ch[i] - srednee)**2
srednekv = (sumkv/len(ch))**0.5
print(s1,srednee,s2,srednekv,s3,maxx,s4,ch.index(maxx),s5,minn,s6,ch.index(minn))