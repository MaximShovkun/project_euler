n = 2000000
prime = []
for i in range(0, n):
    if i == 0 or i == 1:
        prime.append(False)
    else:
        prime.append(True)

i = 2
while i ** 2 < n:
    j = i ** 2
    if prime[i] == True:
        while j < n:
            prime[j] = False
            j += i
    i += 1

sum = 0
k = 0
for i in prime:
    if i == True:
        sum += k
    k += 1

print(sum)