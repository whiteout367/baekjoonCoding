score_dict = {'A+': 4.5, 'A0' : 4.0, 'B+': 3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F': 0.0}
total_scroe = 0
total_credit = 0

for i in range(20):
    input_list = list(map(str, input().split(' ')))
    if input_list[2] != 'P':
        total_credit += float(input_list[1]) 
        total_scroe += float(input_list[1]) *  score_dict[input_list[2]]

print(total_scroe/total_credit)