import sys
import itertools
import wordle, worker

targetWord = ""

try:
    targetWord = sys.argv[1]
except Exception as e:
    print('A problem has occurred from the Problematic code: ', e)
    exit()

wordle_small = open("data/wordle_small.txt")
answerList = [word.strip() for word in wordle_small]
wordle_small.close()

wordle_large = open("data/wordle_large.txt")
possibleList = [word.strip() for word in wordle_large] + answerList
wordle_large.close()

comb = list(itertools.combinations(answerList, 2)) # make list  with unic 2 cards combination

ev = worker.evCalc(targetWord, comb, answerList)

print("\"" + targetWord + "\":" + str(ev))