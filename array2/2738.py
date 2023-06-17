row, column = list(map(int, input().split(' ')))
A = []
B = []
result_list = [[0 for _ in range(column)] for _ in range(row)]

for x in range(0, row):
    A.append(list(map(int, input().split(' '))))

for y in range(0, row):
    B.append(list(map(int, input().split(' '))))

for n in range(0, row):
    for m in range(0, column):
        result_list[n][m] = A[n][m] + B[n][m]
        
for l in result_list:
    print(' '.join(map(str, l)))