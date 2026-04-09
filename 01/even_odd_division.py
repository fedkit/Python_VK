def even_odd_division(l):
    even_list = tuple(filter(lambda x: x % 2 == 0, l))
    odd_list = tuple(filter(lambda x: x % 2 != 0, l))
    return even_list, odd_list