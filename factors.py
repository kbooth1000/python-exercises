import math

num = int(raw_input('A number? '))
half_num = int(num / 2)

for i in range(1, half_num):
    if num % i == 0:
        print i