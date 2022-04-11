import wordle

def evCalc(guess, answerList, aL):
    ev = 0
    mem = {}
    for x,y in answerList:
        divisor = len(answerList)
        xRes = wordle.score(x, guess)
        yRes = wordle.score(y, guess)
        xResTup = tuple(xRes)
        if xResTup in mem.keys():
            ev += mem[xResTup]
        else:
            number = len(wordle.filter_words(aL, guess, xRes))/divisor
            ev += number
            mem[xResTup] = number
        yResTup = tuple(yRes)
        if yResTup in mem.keys():
            ev += mem[yResTup]
        else:
            number = len(wordle.filter_words(aL, guess, yRes))/divisor
            ev += number
            mem[yResTup] = number
    #print(guess + " " + str(ev))
    return ev
