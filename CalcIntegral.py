import random, math
testTimes = 1000000
targetNum = 0
for i in range(0,testTimes):
    x = random.uniform(0, 1)
    y = random.uniform(0, 1)
    #print(x, y, math.sqrt(math.pow(x, 2) + pow(y, 2)))
    if pow(x, 2) >= y:
        targetNum += 1

print("pi = ", targetNum/testTimes)


