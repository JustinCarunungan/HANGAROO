def getAvailableLetters(lettersGuessed):
    import string
    a = string.ascii_lowercase
    s = ''
    for x in a:
        if x not in lettersGuessed:
            s = s + x
    return s