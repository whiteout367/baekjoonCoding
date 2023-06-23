input_int=int(input())

val=1
while input_int>val:
    input_int-=val
    val+=1 
    
if val%2==0:
    a=input_int
    b=val-input_int+1
else:
    a=val-input_int+1
    b=input_int
    
print(f'{a}/{b}')