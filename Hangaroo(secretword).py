def Hangaroo(secretWord):
    import getAvailableLetters
    import getGuessedWord
    import iswordguessed
    print("Let's play Hangaroo! You have 10 tries to guess the word.")
    lettersGuessed = ''
    availLetters = getAvailableLetters.getAvailableLetters(lettersGuessed)        
    tries = 10
    while tries > 0:
        print()
        print("Secret Word : " + getGuessedWord.getGuessedWord(secretWord,lettersGuessed))
        letter = input("Guess a letter : ")
        if letter not in availLetters:
            print("You already used that letter.")
        else:
            if letter not in secretWord:
                print("Wrong letter")
            else:
                lettersGuessed += letter
                availLetters = getAvailableLetters(lettersGuessed)        
        if iswordguessed.isWordGuessed(secretWord,lettersGuessed):
            print("Secret Word : " + getGuessedWord.getGuessedWord(secretWord,lettersGuessed))
            print("Congratulations! You guessed the secret word!") 
            input ("Press any key to exit")
            return
        tries -= 1
        print("Remaining tries : ", + tries)
    else:
        #if tries == 0:
        print("Sorry, game over!")
        input("Press any key to try exit")
    
               
      
    return
Hangaroo("apple")


