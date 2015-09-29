from random import *
ins = open("float_data.txt","w")
s = ""
for i in range(1000000):
    s += str(randint(0,100)) + " "
ins.write(s)
ins.close()
