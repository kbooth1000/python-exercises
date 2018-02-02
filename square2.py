sq_size = int(raw_input('How big is the square (an integer)? '))    
for i in range(0, sq_size):
    row = ''
    for j in range(0, sq_size):
        row = row + '*'
    print row