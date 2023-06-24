n = int(input())

nums_pileup = 1  # 벌집의 개수, 1개부터 시작
cnt = 1
while n > nums_pileup :
    nums_pileup += 6 * cnt  # 벌집이 6의 배수로 증가
    cnt += 1  # 반복문을 반복하는 횟수
print(cnt)

"""
직접 작성한 코드(시간초과 에러)
input_int = int(input())

floar = 1
result = 1

while input_int > floar:
    result += 1
    floar += 6

print(result)
"""