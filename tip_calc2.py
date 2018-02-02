import math

bill = float(raw_input('What\'s the total bill amount? '))
service_level = raw_input('Level of service (good, fair, bad) ')
num_payers = float(raw_input('How many people will divide the bill? '))

if service_level == 'good':
    tip = float(bill * .2)
if service_level == 'fair':
    tip = float(bill * .15)
if service_level == 'bad':
    tip = float(bill * .1)

total_bill = float(bill + tip)
amt_per_payer = total_bill / num_payers

print
print '----------------------'
print 'Tip amount: $%.2f.' % tip
print 'Your total bill with tip is: $%.2f.' % total_bill
print 'Amount per person is: $%.2f.' % amt_per_payer
print '----------------------'
print