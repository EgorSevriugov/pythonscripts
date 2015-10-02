from random import *
ins = open("float_data.txt","w")
s = ""
for i in range(0,1000000):
    s += str(randint(0,10000)/100) + " "
print(s)
ins.write(s)
ins.close()