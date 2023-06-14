dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

insert_str_list = list(input())
result  = 0

for j in insert_str_list:
    for i in dial:
        if j in i:
            result += dial.index(i)+3

print(result)