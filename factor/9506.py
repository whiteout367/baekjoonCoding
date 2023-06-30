while True:
    input_int = int(input())
    if input_int == -1:
        break
    result = []
    
    for i in range(1, input_int+1):
        if input_int % i == 0 and input_int != i:
            result.append(i)

    if sum(result) == input_int:
        print(input_int, '=', ' + '.join(map(str, result)))

    else:
        print(input_int,'is NOT perfect.')