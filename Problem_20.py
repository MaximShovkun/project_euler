from math import factorial

sum = 0
for i in [int(d) for d in str(factorial(100))]:
    sum += i
    
print(sum)
