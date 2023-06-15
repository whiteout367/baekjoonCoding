input_int = int(input())

for i in range(1, input_int):
    print(' '*(input_int-i) + '*'*(2*i-1))

for i in range(input_int, 0, -1):
    print(' '*(input_int-i) + '*'*(2*i-1))