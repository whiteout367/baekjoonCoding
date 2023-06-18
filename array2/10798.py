A = []
max_len = 0
result_str = ''

for _ in range(5):
    input_list = input()
    if max_len < len(input_list):
        max_len = len(input_list)
    A.append(input_list)

for x in range(max_len):
    for y in range(5):
        if len(A[y]) > x:
            result_str += A[y][x]

print(result_str)