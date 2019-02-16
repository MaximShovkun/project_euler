import math as m

c = 0
a = 0
b = 0

while a + b + c < 1000:
    c += 1
    for a in range(1, c):
        b = m.sqrt(c ** 2 - a ** 2)
        if int(b) == b and a + b + c == 1000:
            b = int(b)
            print('\na = {}, b = {}, c = {}'.format(a,b,c))
            print('a^2 = {}, b^2 = {}, c^2 = {}'.format(a**2, b**2, c**2))
            print('{} + {} = {}'.format(a**2, b**2, c**2))
            print('a + b + c = {} + {} + {} = {}'.format(a, b, c, a + b + c))
            print('a * b * c = {}'.format(a * b * c))
            break
