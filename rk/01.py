def three_or_five(nums):
    answer = []
    for i in nums:
        if (i % 3 == 0 or i % 5 == 0) and i % 15 != 0:
            answer.append(i)

    return answer

numbers = [1, 3, 5, 15, -9, 2, 7, 99, 45, 30, 1, -5, 6]
result = three_or_five(numbers)
assert result == [3, 5, -9, 99, -5, 6]