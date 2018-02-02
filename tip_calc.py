bill = int(raw_input('What\'s the total bill amount? '))
service_level = raw_input('Level of service (good, fair, bad) ')

if service_level == 'good':
    tip = bill * .2
if service_level == 'fair':
    tip = bill * .15
if service_level == 'bad':
    tip = bill * .1

total_bill = bill + tip

print 
print 'Tip amount: $%d.' % tip
print 'Your total bill with tip is: $%d.' % total_bill
print