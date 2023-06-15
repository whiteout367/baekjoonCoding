input_str = input().upper()
input_list = list(set(input_str))

count_list = []
for i in input_list:
    count_list.append(input_str.count(i))

if count_list.count(max(count_list)) > 1:
    print("?")
else:
    print(input_list[(count_list.index(max(count_list)))])