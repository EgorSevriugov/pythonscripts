s= str(input())
f = [1] * int(s[0])
for i in range(int(s[2])-int(s[0])+1):
    f.append(int(eval(str(str(f[i:])[1:-1]).replace(",","+"))))
print(f[int(s[2])])