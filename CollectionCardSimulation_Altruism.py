import random
import time
start = time.time()
#############################
# SIMULATION PARAMETERS 
#############################

#Number of iterations
ITERATIONS = 10000
# Number of empty places in album (to every place one card is assigned )
EMPTY_PLACES = 192 
# How many cards buys Julka (how often) in comparison to Zuza. 1 means they buy cards with the same frequency. 
# 0.5 means - number of cards bought by Julka is equal to 50% of number of cards bought by Zuza (so Zuza buys cards two times often then Julka). 
# 0.25 - ... Zuza buys cards four times often then Julka, and so on.
# If number bigger than 1 is set, 1 will be used in simulation. Julka can't buy cards ofthen than Zuza in this simulation. 
JULKA_ZUZKA_RATIO = 1

class Collectioner:

  def __init__(self):
    self.book = [0]*EMPTY_PLACES
    self.completed = False
    self.forExchange = []

  def reset(self):
    self.book = [0]*EMPTY_PLACES
    self.completed = False
    self.forExchange = []

  def drawCard(self,num):
    doIneedIt = True
    self.book[num-1] = self.book[num-1] + 1
    if self.book[num-1] > 1:
      doIneedIt = False
      self.forExchange.append(num)

    return doIneedIt

  def doIneedIt(self,num):
    if self.book[num-1] >0:
      return False
    else:
      return True
      
  def isAnyCardForMe(self,listWithCards):
    indexCardForMe = -1
    size = len(listWithCards)
    for i in range(size-1,-1,-1):
      if self.doIneedIt(listWithCards[i]):
        indexCardForMe = i
        break
    return indexCardForMe
     
  def updateBookCompletedStatus(self):
    isCompleted = True
    for item in self.book:
      if item == 0:
       isCompleted = False
       break
    self.completed = isCompleted

minIterZ = float('inf')
maxIterZ = 0
averageIterZ = 0
minIterJ = float('inf')
maxIterJ = 0
averageIterJ = 0

Zuza = Collectioner()
Julka = Collectioner()


for i in range(ITERATIONS):
  if i%100 == 0:
    print "iteration ",i
  numOfIterationsForZuza = 0
  numOfIterationsForJulka = 0
  Zuza.reset()
  Julka.reset()
  
  while (not Zuza.completed) or (not Julka.completed):
    lastCompletedStatusForZuza = Zuza.completed
    lastCompletedStatusForJulka = Julka.completed
    #  1) DRAW CARD
    if not Zuza.completed:
      Zuza.drawCard(random.randint(1,EMPTY_PLACES))
    if not Julka.completed:
      if Zuza.completed:
        goJulka = True #skip randomization related with frequency 
      elif random.random() < JULKA_ZUZKA_RATIO: #Julka buys a card in 100*JULKA_ZUZKA_RATIO % of cases
        goJulka = True                        #but not more often then Zuza
      else:
        goJulka = False

      if goJulka:
        Julka.drawCard(random.randint(1,EMPTY_PLACES))

    # 2) CHECK CONDITIONS FOR CARD EXCHANGE AND (IF POSSIBLE) DO IT   
    excCardForZ = Zuza.isAnyCardForMe(Julka.forExchange)
    excCardForJ = Julka.isAnyCardForMe(Zuza.forExchange)
    
    #lets take card if needed (altruizm aproach) 
    if excCardForZ != -1:
      Zuza.drawCard(Julka.forExchange.pop(excCardForZ))
    if excCardForJ != -1:
      Julka.drawCard(Zuza.forExchange.pop(excCardForJ))
      
    newCompletedStatusForZuza = Zuza.completed
    newCompletedStatusForJulka = Julka.completed
    
    if not lastCompletedStatusForZuza:
      numOfIterationsForZuza = numOfIterationsForZuza + 1
    if not lastCompletedStatusForJulka:
      if goJulka:
        numOfIterationsForJulka = numOfIterationsForJulka + 1
    
    #Check if book is completed (if yes, change book status)
    Zuza.updateBookCompletedStatus()
    Julka.updateBookCompletedStatus()
    

  if numOfIterationsForZuza < minIterZ:
    minIterZ = numOfIterationsForZuza
  if numOfIterationsForJulka < minIterJ:
    minIterJ = numOfIterationsForJulka
  
  if numOfIterationsForZuza > maxIterZ:
    maxIterZ = numOfIterationsForZuza
  if numOfIterationsForJulka > maxIterJ:
    maxIterJ = numOfIterationsForJulka
    
  averageIterZ = averageIterZ  + numOfIterationsForZuza
  averageIterJ = averageIterJ  + numOfIterationsForJulka
  
      

averageIterZ = averageIterZ / ITERATIONS
averageIterJ = averageIterJ / ITERATIONS

print "minIterZ = ",minIterZ
print "minIterJ = ",minIterJ
print "maxIterZ = ",maxIterZ
print "maxIterJ = ",maxIterJ

print "averageIterZ = ",averageIterZ
print "averageIterJ = ",averageIterJ

end = time.time()
print(end - start)
