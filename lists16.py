n = int(input())
n += 1
ch = [1]
for i in range(n):
    mis = ch[:]
    ch = []
    ch.append(1)
    for k in range(i-1) :
        ch.insert(k+1,eval(str(str(mis[k:k+2])[1:-1]).replace(",","+")))
    ch.append(1)
    if i == 0:
        print(1)
    else:
        print((str(ch[:])[1:-1]).replace(","," "))