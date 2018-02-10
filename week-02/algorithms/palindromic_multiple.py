###  Find the largest palindromic number 
###  made from the product of two 3-digit numbers.


# multiply 999 by 999 -=1...0, then 998 by 998 -=1...0, etc.
# eval if list(str(product)) = reverse(list(str(product)))

finish = False
for factor_1 in range(999, 99, -1):
    for factor_2 in range (999, 99, -1):
        num_str = str(factor_1 * factor_2)
        print '%d * %d = %d' % (factor_1, factor_2, factor_1 * factor_2)
        if num_str == num_str[ : : -1]:
            print '*****  %d * %d = %d' % (factor_1, factor_2, factor_1 * factor_2)
            finish = True
            break
    if finish:
        break
 