def evens(numbers):
    even_nums = []
    for number in numbers:
        if number % 2 == 0:
            even_nums.append(number)
    return even_nums
print
print evens([10,3,34,2,57])
print