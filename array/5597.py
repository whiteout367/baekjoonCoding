studentList = []
for i in range(0, 28):
    studentList.insert(i,int(input()))

sortList = sorted(studentList)

for x in range(0,len(sortList)):
    y = x - 1
    if x != 0:
        if sortList[y] != sortList[x] - 1:
            print(sortList[y] + 1)