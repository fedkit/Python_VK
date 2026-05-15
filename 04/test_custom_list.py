from custom_list import CustomList

# +
assert CustomList([1, 2, 3, 4, 5, 6]) + CustomList([6, 5, 4, 3, 2, 1]) == CustomList([7] * 6)
assert CustomList([22, 33, 44]) + [11, -11] == CustomList([33, 22, 44])
assert [9, 10, 10, 10] + CustomList([1]) == CustomList([10, 10, 10, 10])
assert CustomList([2, 5, -2, 3]) + 7 == CustomList([9, 12, 5, 10])
assert 13 + CustomList([2, 0, 3]) == CustomList([15, 13, 16])

# -
assert CustomList([8, 3, 6, 10, 4]) - CustomList([2, 5, 7, 1]) == CustomList([6, -2, -1, 9, 4])
assert CustomList([14, 9, 2]) - [3, 11, 1, 5] == CustomList([11, -2, 1, -5])
assert [6, 12, 4, 8] - CustomList([15, 3]) == CustomList([-9, 9, 4, 8])
assert CustomList([7, 11]) - 5 == CustomList([2, 6])
assert 20 - CustomList([4, 9, 1, 6]) == CustomList([16, 11, 19, 14])

# ==
assert CustomList([4, 1, 2, 3]) == CustomList([10])
assert CustomList([2, 2, 2]) == CustomList([3, 3])
assert CustomList([5]) == CustomList([2, 3])

# >=
assert CustomList([4, 1, 2, 3]) >= CustomList([9])
assert CustomList([5, 5]) >= CustomList([4, 6])
assert CustomList([10]) >= CustomList([9, 1])

# >
assert CustomList([15]) > CustomList([3, 4, 5])
assert CustomList([8, 3]) > CustomList([5, 5])
assert CustomList([7, 7]) > CustomList([13])

# <=
assert CustomList([2, 3, 1]) <= CustomList([7])
assert CustomList([1, 2, 3]) <= CustomList([10])
assert CustomList([4, 4]) <= CustomList([10])

# <
assert CustomList([5, 2]) < CustomList([20, 1])
assert CustomList([1, 1, 1]) < CustomList([5])
assert CustomList([2, 3]) < CustomList([10])

# !=
assert CustomList([6, 1, 2]) != CustomList([5, 5])
assert CustomList([1, 2, 3]) != CustomList([10])
assert CustomList([4, 4]) != CustomList([3, 6])

# str
assert str(CustomList([1, 2, 3])) == '[1, 2, 3]\nSum:6'
assert str(CustomList([10])) == '[10]\nSum:10'
assert str(CustomList([])) == '[]\nSum:0'
assert str(CustomList([4, -3, 9, -1])) == '[4, -3, 9, -1]\nSum:9'
assert str(CustomList([0, -2, 2])) == '[0, -2, 2]\nSum:0'
