#Imports
from scipy.stats import qmc
import math
import numpy
import wordle, worker
from multiprocessing import Pool
import os

#Seed the generator so that results are consistent
sobolGen = qmc.Sobol(2, scramble=True, seed=0)
haltonGen = qmc.Halton(2, scramble=True, seed=0)
numpy.random.seed(0)

#Set up
pairsToGen = 2048

wordle_small = open("data/wordle_small.txt")
answerList = [word.strip() for word in wordle_small]
wordle_small.close()

wordle_large = open("data/wordle_small.txt")
possibleList = [word.strip() for word in wordle_large]
wordle_large.close()

l_bounds = [0,0]
u_bounds = [len(answerList) for _ in range(0,2)]

sobolSample = sobolGen.random(pairsToGen)
sobolSampleScaled = qmc.scale(sobolSample, l_bounds, u_bounds)
sobolWords = [(answerList[math.floor(x)], answerList[math.floor(y)])for x,y in sobolSampleScaled]

haltonSample = haltonGen.random(n=pairsToGen)
haltonSampleScaled = qmc.scale(haltonSample, l_bounds, u_bounds)
haltonWords = [(answerList[math.floor(x)], answerList[math.floor(y)])for x,y in haltonSampleScaled]

randomSample = numpy.random.randint(0, len(answerList), size=(pairsToGen,2))
randomWords = [(answerList[x], answerList[y]) for x,y in randomSample]

sobolCount = {}
for tup in sobolWords:
    for word in tup:
        if word in sobolCount.keys():
            sobolCount[word] += 1
        else:
            sobolCount[word] = 1
print("Unique sobol words: " + str(len(sobolCount)))

haltonCount = {}
for tup in haltonWords:
    for word in tup:
        if word in haltonCount.keys():
            haltonCount[word] += 1
        else:
            haltonCount[word] = 1
print("Unique halton words: " + str(len(haltonCount)))

randomCount = {}
for tup in randomWords:
    for word in tup:
        if word in randomCount.keys():
            randomCount[word] += 1
        else:
            randomCount[word] = 1
print("Unique random words: " + str(len(haltonCount)))

evsMap = {}
with Pool(processes=15) as p:
    evs = p.starmap(worker.evCalc, [(i, answerList) for i in possibleList])
    print("Processing done!")
    for i in range(len(evs)):
        evsMap[possibleList[i]] = evs[i]
print(evsMap)