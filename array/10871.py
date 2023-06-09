listCount, comInt = list(map(int, input().split()))
intList = list(map(int, input().split()))
resultList = [int(x) for x in intList if comInt > x]

resultString = ' '.join(map(str,resultList))
print(resultString)
