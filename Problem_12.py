def triang_num(index):
    return (index * (index + 1)) / 2
	
def num_of_factors(number):
    n = number
    result_list = []
    sqrt_n = int(n ** 0.5)
    for i in range(1, sqrt_n + 1):
        if n % i == 0:
            result_list.append(n / i)
            result_list.append(i)
    return len(result_list)
	
n = 0
while num_of_factors(triang_num(n)) <= 500:
    n += 1
print triang_num(n)
print n