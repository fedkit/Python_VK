from create_uniquge_list import merge


def run_test(lst1, lst2, answer):
    assert merge(lst1, lst2) == answer


# 1
lst1 = [1, 1, 2, 5, 7]
lst2 = (1, 1, 2, 3, 4, 7)
answer1 = [1, 2, 7]
run_test(lst1, lst2, answer1)


# 2 
lst1 = [1000, 1000, 1000]
lst2 = [1000, 1000]
answer2 = [1000]
run_test(lst1, lst2, answer2)


# 3 
lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
answer3 = []
run_test(lst1, lst2, answer3)


# 4 
lst1 = [-10, -5, -3, -3, 0, 2, 4, 7, 10, 15, 20, 25]
lst2 = [-8, -5, -5, -3, 1, 2, 2, 3, 7, 10, 12, 20, 30]
answer4 = [-5, -3, 2, 7, 10, 20]
run_test(lst1, lst2, answer4)


# 5 
lst1 = [1, 1, 1, 2, 2, 3]
lst2 = [1, 1, 2, 2, 2, 3, 3]
answer5 = [1, 2, 3]
run_test(lst1, lst2, answer5)


# 6
lst1 = []
lst2 = [1, 2, 3]
answer6 = []
run_test(lst1, lst2, answer6)
