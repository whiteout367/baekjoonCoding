resultArr = []
finalArr = []
for _ in range(10):
    incomeInt = int(input()) % 42
    resultArr.append(incomeInt)

# 그냥 함수 1줄이면 됩니다.
# 순서 있으면 list(dict.fromkeys(array)) 없으면 list(set(array))
# finalArr = list(dict.fromkeys(resultArr))
for x in resultArr:
    if x not in finalArr:
        finalArr.append(x)
            
print(len(finalArr))