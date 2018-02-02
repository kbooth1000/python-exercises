start_num = int(raw_input('Start number: '))
end_num = int(raw_input('End number: '))

if start_num >= end_num:
    print 'Please make sure the end number is larger than the start number.'

for i in range(start_num, end_num):
    print i