from even_odd_division import even_odd_division

assert even_odd_division([]) == ((), ())
assert even_odd_division([12, 34, 6, -8]) == ((12, 34, 6, -8), ())
assert even_odd_division([11, 887, -133, -1]) == ((), (11, 887, -133, -1))
assert even_odd_division([9, 8, 7, 6, 5, 4]) == ((8, 6, 4), (9, 7, 5))
assert even_odd_division(list(range(10))) == ((0, 2, 4, 6, 8), (1, 3, 5, 7, 9))
