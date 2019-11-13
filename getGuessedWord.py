def getGuessedWord(secretWord,lettersGuessed):
    s = ''
    for x in secretWord:
        if x in lettersGuessed:
            s = s + x
        else:
            s = s + '_ '
    return s
