import random
EMPTY_PLACES = 192
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
        tmpCard = random.randint(1,EMPTY_PLACES)
        wholeBook[tmpCard-1] = wholeBook[tmpCard-1] + 1
        counter = counter + 1

    return counter

tmpNumber = fillInWholeBook()
minNumber = tmpNumber
maxNumber = tmpNumber
averageNumber = tmpNumber
for i in range(9999):
    tmpNumber = fillInWholeBook()
    if tmpNumber < minNumber:
        minNumber = tmpNumber

    if tmpNumber > maxNumber:
        maxNumber = tmpNumber

    averageNumber = averageNumber + tmpNumber

averageNumber = averageNumber / 10000

print "minNumber ", minNumber
print "maxNumber", maxNumber
print "averageNumber", averageNumber




    

        
    
