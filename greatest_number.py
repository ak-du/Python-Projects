# Problem statement
# find the greatest number among the three given numbers

a = 101
b = 101
c = 100
# comparison of the three values
if a > b:
    if a > c:
        print('a')
    else:
        print('c')
elif b > c:
    print('b')
elif a == b == c:
    print('All are equal')
else:
    print('c')