

# x=0
# j=0
# for i in range(1,20):
#     z = 0
#     x += 20
#     while x % i == 0:
#         print x % i
#         z += 1
#         print z
#         if z >= 20:
#             print '******'
#             print x
#             break

x=0
j=0
while True:
    z=0
    x+=20
    for i in range(1,20):
        num = x % i
        if num == 0:
            z += 1
        if z == 20:
            break
    break
print x
        

# n=0
# while True:
#     n += 20
#     correct = True
#     for x in range (1, 20):
#         if n % x != 0:
#             correct = False
#             break

#     if correct:
#         break
# print n
