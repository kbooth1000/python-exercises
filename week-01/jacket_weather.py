temperature = int(raw_input('Temperature: '))
if temperature < 30:
    print 'Wear a heavy coat.'
elif temperature < 55:
    print 'Wear a jacket.'
else:
    print 'No jacket needed.'

print temperature