a, b, v = list(map(int, input().split()))
result = (v-b)/(a-b)
print(int(result) if result == int(result) else int(result) + 1)