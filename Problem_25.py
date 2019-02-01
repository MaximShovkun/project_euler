import time
start_time = time.time()


def better_fib(n):
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[n]


i = 0
while True:
    i += 1
    if len(str(better_fib(i))) == 1000:
        print(i)
        break


print ("time elapsed: {:.2f}s".format(time.time() - start_time))