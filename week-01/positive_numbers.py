def positives(numbers):
    positive_nums = []
    for number in numbers:
        if number > 0:
            positive_nums.append(number)
    return positive_nums
print
print positives([10,-3,-34,2,57])
print