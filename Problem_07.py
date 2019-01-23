import math as m

def is_prime(number1):
    sqrt_of_number = int(m.sqrt(number1))
    for i in range(2, sqrt_of_number + 1) :
        if number1 % i == 0:
            return False
    return True

count = 0
i = 1
while count < 10001:
    i += 1
    if is_prime(i):
        count += 1
print i