input_int, key = map(int, input().split())
result = []
for i in range(1, input_int+1):
    if input_int % i == 0:
        result.append(i)

if len(result) > key - 1:
    print(result[key - 1])
else:
    print(0)