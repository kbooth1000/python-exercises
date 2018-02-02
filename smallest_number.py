def smallest(numbers):
    smallest_num = 99999999999
    for number in numbers:
        if number < smallest_num:
            smallest_num = number
    return smallest_num
print
print smallest([10,3,34,2,52])
print