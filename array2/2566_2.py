A = []
result_val = 0
result_row = 0
result_column = 0

for _ in range(9):
    A.append(list(map(int, input().split(' '))))
    
for i in range(0,len(A)):
    for j in range(0,len(A[i])):
        if A[i][j] > result_val:
            result_val = A[i][j]
            result_row = i
            result_column = j
            
print(result_val)
print(result_row+1, result_column+1)