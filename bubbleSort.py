import random

def bubbleSort(list):
    n = len(list)
    while n > 0:
        for i in range (0, n-1):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
        n -= 1

    return list



def populate():
    x = []
    for i in range (0, 100):
        x.append(round(random.random()*10000))
    return x
    


x = populate()

print x

print bubbleSort(x)
