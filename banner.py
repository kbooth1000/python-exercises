banner_text = raw_input('What should the banner say? ')
banner_length = len(banner_text) + 2

print
for i in range(0, 3):
    row = ''
    for j in range(0, banner_length-1):
        if i == 0 or i == 2:
            row = row + '*'
        else:
            if j > 0 and j < banner_length:
                row = row + banner_text[j-1]
            else:
                row = row + '*'
    row = row + '*'
    print row
print