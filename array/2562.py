intList = []
for x in range(9):
    insertInt = int(input())
    intList.insert(x, insertInt)
    
print(max(intList))
print(intList.index(max(intList))+1)