total_list = [1, 1, 2, 2, 2, 8]
count_list = list(map(int, input().split()))
result_list = []

for a, b in zip(total_list, count_list):
    result_list.append(a-b)

print(' '.join(map(str,result_list)))