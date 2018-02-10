###   What is the smallest positive number 
###   that is evenly divisible by 
###   all of the numbers from 1 to 20?



increment_num = 20     
for x in range(20, 1, -1):  
    print 'x = %d' % x 
    i = 1
    while True:
        
        if (i * increment_num) % (x - 1) != 0:
            i += 1
        else:
            increment_num = (i * increment_num)
            print 'increment num: %d' % increment_num
            break
print i*increment_num