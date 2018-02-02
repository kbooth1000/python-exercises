import math

odd = 1
for i in range(0, 4):
    row = ''
    for j in range(0, 7):
        if j > (math.floor(7/2) - odd) and j < (math.floor(7/2) + odd):
            row = row + '*'
        else:
            row = row + ' '
    odd += 1
    print row