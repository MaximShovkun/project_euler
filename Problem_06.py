n = 0
k = 0
for i in range(1, 101):
    n = n + i ** 2
    k = k + i

print('Sum of the squares = {}'.format(n))
print('Square of the sum = {}'.format(k ** 2))
print('Difference = {}'.format(k ** 2 - n))
