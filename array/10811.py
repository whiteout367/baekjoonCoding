list_count, input_int = list(map(int, input().split()))

bucket = [i for i in range(1,list_count + 1)]
after_bucket = []
        
for _ in range(input_int):
    a, b = list(map(int, input().split()))
    after_bucket = list(reversed(bucket[a-1:b]))
    bucket[a-1:b] = after_bucket

print(' '.join(str(e) for e in bucket))