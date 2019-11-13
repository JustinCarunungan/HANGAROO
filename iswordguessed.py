def isWordGuessed(secretWord,lettersGuessed):
    for x in lettersGuessed:
        if x not in secretWord:
            return False
    for x in secretWord:
        if x not in lettersGuessed:
            return False
    return True
        