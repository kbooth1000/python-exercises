# multiply 999 by 999 -=1
# eval if list(str(m)) = reverse(list(str(m)))

finish = False
for m in range(999, 99, -1):
    for n in range (999, 99, -1):
        num_str = str(m * n)
        print '%d * %d = %d' % (m, n, m*n)
        if num_str == num_str[ : : -1]:
            print '*****  %d * %d = %d' % (m, n, m*n)
            finish = True
            break
    if finish:
        break
 