coins = 0
want = True
while want:
    print 'You have %d coins.' % coins
    want_coin = raw_input('Do you want another? ').upper()
    if want_coin == 'YES':
        coins += 1
        want = True
    else:
        want = False
print 'Bye.'