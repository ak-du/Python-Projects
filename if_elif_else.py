# Problem statement
# If the number is divisible bt 3 print 3, if its divisible by 5 print 5 if its divisible by both print both
# if its not divisible by any print not divisible

number = 15

if number%3 == 0 and number%5 == 0:
    print('both')
elif number%5 == 0:
    print(5)
elif number%3 == 0:
    print(3)
else:
    print('not divisible')






