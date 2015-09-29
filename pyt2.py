x= int(input())
i = 0
li = 0
num = 0
long = None
last = None
last2 = None
while x != 0:
    num += 1
    if last == None:
        last = x
    elif last2 == None:
        last2,last = last, x
    elif last > x and last > last2:
        if i != li:
            i,li = num - 1,i
        else :
            i = num - 1
    if i != 0 and li != 0:
        if long == None:
            long = i - li
        elif (i - li) < long:
            long = i - li
        li,i = 0,0
    last,last2 = x, last
    x = int(input())
else:
    if long == None:
        print(0)
    else:
        print(long)