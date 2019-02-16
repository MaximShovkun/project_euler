import math as m

num = 600851475143
num_root = m.sqrt(num)

for i in range(int(num_root) + 1, 2, -1):
    if num % i == 0:
        for k in range(2, i//2 + 1):
            if i % k == 0:
                break
        else:
            print(i)
            break
