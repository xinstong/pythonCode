import random, math
testTimes = 100000
targetNum = 0
for i in range(0,testTimes):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    #print(x, y, math.sqrt(math.pow(x, 2) + pow(y, 2)))
    if (math.sqrt(math.pow(x, 2) + pow(y, 2)) < 1.0):
        targetNum += 1

print("pi = ", targetNum*4/testTimes)


