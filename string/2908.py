insert_str_list = list(map(str, input().split(' ')))

reverse_str1 = int(insert_str_list[0][::-1])
reverse_str2 = int(insert_str_list[1][::-1])

if reverse_str1 >= reverse_str2:
    print(reverse_str1)
    
else:
    print(reverse_str2)