lenList = int(input())
intList = list(map(int, input().split()))
sortedList = sorted(intList)
indexOfBIg = lenList - 1

print(sortedList[0], sortedList[indexOfBIg])