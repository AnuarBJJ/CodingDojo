import random
import datetime

def insertionSort(list):
    for i in range (1, len(list)):
        for j in range (i, 0, -1):
            while list[j] < list [j-1]:               
                list[j], list [j-1] = list [j-1],  list[j]
                
    return list



def populate():
    x = []
    for i in range (0, 100):
        x.append(round(random.random()*10000))
    return x
    
x = populate()

print x

t1 = datetime.datetime.now()

print insertionSort(x)

t2 = datetime.datetime.now()

print t2 - t1
