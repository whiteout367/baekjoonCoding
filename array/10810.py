listCount, comInt = list(map(int, input().split()))

bucket = [0] * listCount
for x in range(comInt):
    bList = list(map(int, input().split()))
    for y in range(bList[0]-1,bList[1]):
        bucket[y] = bList[2]
        
print(' '.join(str(e) for e in bucket))