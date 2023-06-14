import string

insertStr = str(input())
result = ''

for i in string.ascii_lowercase[:26]:
    result += str(insertStr.find(i))
    result += ' '
print(result)