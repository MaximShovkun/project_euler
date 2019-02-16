maxDiv = 20
minStep = maxDiv * (maxDiv - 1)
minNum = minStep
count = 0
while count != maxDiv - maxDiv // 2:
    for i in range(maxDiv, maxDiv // 2, -1):
        if minNum % i == 0:
            count = count + 1
        else:
            count = 0
            minNum = minNum + minStep
            break
print(minNum)
