box_w = int(raw_input('How wide is the box (an integer)? '))
box_h = int(raw_input('How high is the box (an integer)? '))
for i in range(0, box_h):
    row = ''
    for j in range(0, box_w):
        if i != 0 and i != (box_h - 1):
            if j == 0 or j == (box_w - 1):
                row = row + '*'
            else:
                row = row + ' '
        else:
            row = row + '*'
    print row