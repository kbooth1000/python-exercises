import math

triangle_h = int(raw_input('How many rows in the triangle? '))
num_cols = triangle_h + (triangle_h + 1)

odd = 1
for i in range(0, triangle_h):
    row = ''
    for j in range(0, num_cols):
        if j > (math.floor(num_cols/2) - odd) and j < (math.floor(num_cols/2) + odd):
            row = row + '*'
        else:
            row = row + ' '
    odd += 1
    print row