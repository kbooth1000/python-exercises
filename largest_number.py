def largest(numbers):
    largest_num = 0
    for number in numbers:
        if number > largest_num:
            largest_num = number
    return largest_num
print
print largest([10,3,34,2,52])
print