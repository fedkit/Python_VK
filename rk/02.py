def gen_filter(data, is_valid, n):
    k = 0
    for i in data:
        if is_valid(i):
            yield i
            k += 1
            if k == n:
                return
            
gen = gen_filter([1, -2, -3, 5, 0, 4, -9, 6], lambda x: x > 0, 3) 
for i in gen: 
    print(i)