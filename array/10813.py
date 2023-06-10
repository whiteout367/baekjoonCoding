listCount, comInt = list(map(int, input().split()))

bucket = [0] * listCount
for i in range( listCount):
    bucket[i] = (i + 1)
    
print(bucket)

for x in range(comInt):
    index1, index2 = list(map(int, input().split()))
    index11 = index1 - 1
    index12 = index2 - 1
    a = bucket[index11]
    b = bucket[index12]
    bucket[index12] = a
    bucket[index11] = b
    print(bucket)
    
print(' '.join(str(e) for e in bucket))