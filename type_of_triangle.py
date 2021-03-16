# Problem statement
# To find the type of triangles-Isosceles, equilateral or scalene

side1 = 4
side2 = 4
side3 = 4

if side1 == side2 == side3:
    print('It is an equilateral triangle')
elif (side1 == side2) or (side2 == side3) or (side1 == side3):
    print('It is an Isosceles triangle')
else:
    print('It is a scalene triangle')
