import random
import datetime

def selectionSort(list):

    j = 0
    while j < (len(list)-1)/2:
        min = list[j]
        max = list[len(list)-j-1]

        for i in range (j, len(list)-1-j):
        
            if list[i+1] < min:
                min = list[i+1]
                indexMin = i+1
                
            if list[i+1] > max:
                max = list[i+1]
                indexMax = i+1
                
        list[j], list[len(list)-j-1], list[indexMin], list[indexMax] = list[indexMin], list[indexMax], list[j], list[len(list)-j-1]

        j += 1
    
    return list



def populate():
    x = []
    for i in range (0, 100):
        x.append(round(random.random()*10000))
    return x
    
x = populate()

print x

t1 = datetime.datetime.now()

print selectionSort(x)

t2 = datetime.datetime.now()

print t2 - t1
