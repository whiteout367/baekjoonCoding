a, b = input().split()
ary = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

a = a[::-1]
result = 0

for x,y in enumerate(a):
    result += (int(b)**x)*(ary.index(y))
print(result)