# CardSimulation
Imagine album for sticker collection, for example my daughter (Zuzia) has album with 192 empty enumerated places 
for (enumerated) stickers with Monster High creatures:-). 
You can buy stickers in foiled boosters, so you don't know which sticker you draw. On the begining almost every sticker is new and you can put 
it in empty place (with the same number as on stick) in album. Later situation will become more difficult - often you already have this drawn card. On the end it's hard to complete missing stickers. 

The question is - how many stickers you need to buy to complete whole album with 192 empty places for 192 different stickers. 
## Simulation for one person 
CollectionCardSimulation.py script makes simulation: one iteration is related with experiment - draw random cards untill all places in album are fulfilled. This iteration is repeated 10000 times (EMPTY_PLACES = 192 and NUM_ITERATIONS = 10000 are parameters of smulation which can be changed in script). 
Minimum value of cards, maximum and average are printed. 

## Simulation for two persons colaborating in 'cooperation mode'
Now lets take two persons: Zuza and her friend Julka. They will exchange cards with 'cooperation rule': if Zuza has not needed card which is needed by Julka AND Julka has not needed card which is needed by Zuza    -> they will exchange it to each other. 

CollectionCardSimulation_Cooperation.py simulates this situation. There are three parameters for this simulation on the beginig of the script:
EMPTY_PLACES = 192 and NUM_ITERATIONS = 10000, and additionally JULKA_ZUZKA_RATIO = 1 means how many cards buys Julka (how often) in comparison to Zuza. 1 means they buy cards with the same frequency. 0.5 means - number of cards bought by Julka is equal to 50% of number of cards bought by Zuza (so Zuza buys cards two times often then Julka). 0.25 - ... Zuza buys cards four times often then Julka, and so on. If number bigger than 1 is set, 1 will be used in simulation. Julka can't buy cards ofthen than Zuza in this simulation.

## Simulation for two persons colaborating in 'altruism mode'
This time Zuza and Julka exchange cards in 'altruism mode': If Zuzia has not needed card, they can be taken by Julka even if she hasn't card (needed by Zuzia) for exchange in this moment. The same rule is for Julka -> Zuzia direction. 
All parameters descibed in previous chapter are also valid here. 