import wordle

def evCalc(guess, answerList, aL):
    ev = 0
    mem = {}
    for x,y in answerList:
        divisor = len(answerList)
        xRes = wordle.score(x, guess)
        yRes = wordle.score(y, guess)
        
        val = 1/divisor
        
        xResTup = tuple(xRes)
        if xResTup in mem.keys():
            val *= mem[xResTup]
        else:
            number = len(wordle.filter_words(aL, guess, xRes))
            val *= number
            mem[xResTup] = number
        yResTup = tuple(yRes)
        if yResTup in mem.keys():
            val *= mem[yResTup]
        else:
            number = len(wordle.filter_words(aL, guess, yRes))
            val *= number
            mem[yResTup] = number
            
        ev += val
    #print(guess + " " + str(ev))
    return ev
