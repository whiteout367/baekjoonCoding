c_alpa = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
come_str = input()

for x in c_alpa:
    if x in come_str:
        come_str = come_str.replace(x, '0')
        
print(len(come_str))