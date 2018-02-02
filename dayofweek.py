day = int(raw_input('Day of Week (0-6): '))

if day == 0:
    day_word = 'Sunday'
if day == 1:
    day_word = 'Monday'
if day == 2:
    day_word = 'Tuesday'
if day == 3:
    day_word = 'Wednesday'
if day == 4:
    day_word = 'Thursday'
if day == 5:
    day_word = 'Friday'
if day == 6:
    day_word = 'Saturday'

print 'Today is %s.' % day_word