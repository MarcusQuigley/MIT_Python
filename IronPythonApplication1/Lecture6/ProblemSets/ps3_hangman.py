# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "C:\Users\Marcus\Documents\Visual Studio 2013\Projects\PythonApplication3\IronPythonApplication1\Lecture6\ProblemSets\words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    secretWordAsSet = set(list(secretWord))
    for letter in secretWordAsSet:
        if letter not in lettersGuessed:
            return False
    return True



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    guessedCharsSet = set(secretWord).intersection(lettersGuessed)
    secretWordGuessedList = []
    guessedWordSoFar = ""
    for letter in secretWord:
        if (letter in guessedCharsSet):
            secretWordGuessedList.append(letter + " ")
        else:
            secretWordGuessedList.append("_ ")

    return guessedWordSoFar.join(secretWordGuessedList)



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    lettersNotGuessedString = ""
    lettersGuessedSet = set(lettersGuessed)
    allLettersSet = set(string.ascii_lowercase)

    lettersNotGuessed = list(allLettersSet - lettersGuessedSet)# [x for x in allLettersSet if x not in lettersGuessedSet]
    lettersNotGuessed.sort()
    
    return lettersNotGuessedString.join(lettersNotGuessed)


def letterInSecretWord(secretWord, letter):
   '''
   secretWord: string, the word the user is guessing
   letter: the letter the player has choosen
   returns bool whether secretWord contains the letter
   '''
   return (secretWord.find(letter) > -1)


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    lettersGuessed = []
    guessesMade = 0
    maxGuesses = 8

    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is " + str(len(secretWord)) + " letters long"

    while (guessesMade < maxGuesses):
        print "-------------"
        if (isWordGuessed(secretWord, lettersGuessed)):
            print "Congratulations, you won!"
            break
        else:
            print "You have " + str(maxGuesses - guessesMade) + " guesses left."
            print "Available letters: " + getAvailableLetters(lettersGuessed)
            letterGuessed =string.lower(raw_input("Please guess a letter: "))

            if (letterGuessed in lettersGuessed):
                print "Oops! You've already guessed that letter: ",
             #   print getGuessedWord(secretWord, lettersGuessed)
            else:
                lettersGuessed.append(letterGuessed)
                if (letterInSecretWord(secretWord, letterGuessed)):
                    print "Good guess: ",
                else:
                    guessesMade+=1
                    print "Oops! That letter is not in my word:",
            print getGuessedWord(secretWord, lettersGuessed)
    
    if (guessesMade == maxGuesses):
        print "-------------"
        print("Sorry, you ran out of guesses. The word was "),
        print secretWord






# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord ="cheetah"# chooseWord(wordlist).lower()
hangman(secretWord)
'''
secretWord = chooseWord(
usedLetters = ["a", "c", "b", "o", "e", "h" ]
print isWordGuessed(secretWord, usedLetters)

#print(getGuessedWord(secretWord, usedLetters))
print(getAvailableLetters(secretWord))
'''