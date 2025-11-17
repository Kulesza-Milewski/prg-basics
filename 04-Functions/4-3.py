###
# Calculates the area of a triangle based on the lengths
# of the triangle's sides
#

import math

def triangle_area(a,b,c):
    s = (a + b + c) / 2
    area = math.sqrt(s *(s-a)*(s-b)*(s-c))
    return area

side_a = float(input('geve me side a: '))
side_b = float(input('geve me side b: '))
side_c = float(input('geve me side c: '))

area = triangle_area(side_a,side_b,side_c)

print(f'The area of ​​a triangle with sides {side_a},{side_b},{side_c} is {triangle_area}')