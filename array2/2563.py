A = [[0 for _ in range(101)] for _ in range(101)]
result = 0
paper_count = int(input())

for _ in range(paper_count):
    width, height = list(map(int, input().split(' ')))
    
    for x in range(width, width+10):
        for y in range(height, height+10):
            A[x][y] = 1

for i in A:
    result += i.count(1)

print(result)