import wordle

def evCalc(guess, answerList):
    divisor = len(answerList)
    ev = 0
    for solution in answerList:
        response = wordle.score(solution, guess)
        remaining = wordle.filter_words(answerList, guess, response)
        ev += len(remaining)/divisor
    print(guess + " " + str(ev))
    return ev