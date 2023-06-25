input_int = int(input())

result = 2

while input_int > 0:
    result = result + 2 ** (input_int-1)
    input_int -= 1

print(result ** 2)