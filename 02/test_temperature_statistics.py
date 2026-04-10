from temperature_statistics import temperature_statistics


def run_test(test, answer):
    assert temperature_statistics(test) == answer


# 1
test1 = [12.5, 15, 10.1, 14.9, 16.234, 18, 13.0]
answer1 = {
    'avg': 14,
    'min': 10,
    'max': 18,
    'above_avg': [15, 14.9, 16.234, 18],
    'above_avg_idx': [1, 3, 4, 5]
}
run_test(test1, answer1)


# 2
test2 = [1000, 1000, 1000, 1000, 1000, 1000, 1000]
answer2 = {
    'avg': 1000,
    'min': 1000,
    'max': 1000,
    'above_avg': [],
    'above_avg_idx': []
}
run_test(test2, answer2)


# 3
test3 = [-5, -10, 0, 5, 10]
answer3 = {
    'avg': 0,
    'min': -10,
    'max': 10,
    'above_avg': [5, 10],
    'above_avg_idx': [3, 4]
}
run_test(test3, answer3)


# 4
test4 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
answer4 = {
    'avg': 28,  
    'min': 5,
    'max': 50,
    'above_avg': [30, 35, 40, 45, 50],
    'above_avg_idx': [5, 6, 7, 8, 9]
}
run_test(test4, answer4)


# 5
test5 = [1.2, 1.2, 1.2, 2.8]
answer5 = {
    'avg': 2,  
    'min': 1,
    'max': 3,
    'above_avg': [2.8],
    'above_avg_idx': [3]
}
run_test(test5, answer5)


# 6
test6 = []
answer6 = {
    'avg': None,  
    'min': None,
    'max': None,
    'above_avg': None,
    'above_avg_idx': None
}
run_test(test6, answer6)
