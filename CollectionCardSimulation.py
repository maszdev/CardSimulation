import random
import time
start = time.time()
#############################
# SIMULATION PARAMETERS 
#############################

# Number of empty places in album (to every numerated place one card (with the same number) can be assigned )
EMPTY_PLACES = 192
#Number of iterations
NUM_ITERATIONS = 10000

def isBookComplete(book):
    isComplete = True
    for item in book:
        if item == 0:
            isComplete = False
            break
    return isComplete

def fillInWholeBook():
    wholeBook = [0]*EMPTY_PLACES
    counter = 0
    while not isBookComplete(wholeBook):
        tmpCard = random.randint(0,EMPTY_PLACES-1)
        wholeBook[tmpCard] = wholeBook[tmpCard] + 1
        counter = counter + 1

    return counter

tmpNumber = fillInWholeBook()
minNumber = tmpNumber
maxNumber = tmpNumber
averageNumber = tmpNumber
for i in range(NUM_ITERATIONS-1):
    if i % 1000 == 0:
        print "iteration ",i
    tmpNumber = fillInWholeBook()
    if tmpNumber < minNumber:
        minNumber = tmpNumber

    if tmpNumber > maxNumber:
        maxNumber = tmpNumber

    averageNumber = averageNumber + tmpNumber

averageNumber = averageNumber / NUM_ITERATIONS

print "minNumber ", minNumber
print "maxNumber", maxNumber
print "averageNumber", averageNumber

end = time.time()
print(end - start)




    

        
    
