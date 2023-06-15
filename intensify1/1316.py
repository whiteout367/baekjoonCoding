come_int = int(input())
result = 0
error = 0
for x in range(come_int):
    come_str = input()
    for a in range(0, len(come_str)-1):  
        
        if come_str[a] != come_str[a+1]:
            if come_str[a] in come_str[a+1:]:
                
                error += 1
    if error == 0:  
        result += 1
    error = 0
        
print(result)