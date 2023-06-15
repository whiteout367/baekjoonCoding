come_int = int(input())
result_list = []
a = 0

for i in range(come_int):
    score_list = list(map(int, input().split(' ')))
    sudent_count = score_list[0]
    mean = float((sum(score_list) - sudent_count) / sudent_count)
    for x in score_list[1:]:
        
        if x > mean:
            a += 1
    result_list.append(float(a / sudent_count * 100))
    a = 0
    
for y in result_list:
    print(f'{round(y, 3):.3f}%')
