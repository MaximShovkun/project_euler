max_length = 0
starting_num = 0
for num in range(1, 1000001):
    length = 1
    n = num
    while True:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        length += 1
        if n == 1:
            if length > max_length:
                max_length = length
                starting_num = num
            break
print ("Starting num: {}".format(starting_num))
print ("Length of the chain: {}".format(max_length))