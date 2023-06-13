list_count = int(input())
score = list(map(int, input().split()))
after_list = []
max_score = max(score)
for i in score:
    after_scroe = float(i / max_score * 100)
    after_list.append(after_scroe)
    

print(float(sum(after_list)) / list_count)