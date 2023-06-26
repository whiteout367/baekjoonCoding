coin = [25, 10, 5, 1]
input_int = int(input())

for _ in range(input_int):
    input_bill = int(input())
    for i in coin:
        print(input_bill//i, end=' ')
        input_bill = input_bill%i