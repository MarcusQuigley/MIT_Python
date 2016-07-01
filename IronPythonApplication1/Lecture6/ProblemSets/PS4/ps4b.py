from ps4a import *
import time


#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    bestScore = 0
    bestWord = ""
    # Create a new variable to store the maximum score seen so far (initially 0)
    # Create a new variable to store the best word seen so far (initially None)  

    for word in wordList:
        if (isValidWordinWordList(word, hand)):
                wordScore = getWordScore(word, n)
                if (wordScore > bestScore):
                    bestScore = wordScore
                    bestWord = word


        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)

            # Find out how much making that word is worth

            # If the score for that word is higher than your best score

                # Update your best score, and best word accordingly

    if (bestScore>0):
        return bestWord
    else:
        return None
    # return the best word you found.

def testcompChooseWord(wordList):
    print compChooseWord({'i': 3, 'k': 1, 'd': 1, 'n': 1}, wordList, 6)
    print "----------------"
    print compChooseWord({'a': 1, 'd': 2, 'i': 2, 'k': 1, 'o': 1, 'n': 1}, wordList, 8)
    print "----------------"

    print compChooseWord({'a': 1, 'd': 1, 'i': 1, 'k': 1, 'o': 1, 'n': 1, 'y': 1}, wordList, 7)
    print "----------------"
    print compChooseWord({'q': 1}, wordList, 1)
    print "----------------"
    print compChooseWord({'a': 1, 'p': 2, 's': 1, 'e': 1, 'l': 1}, wordList, 6)
    print "----------------"
    print compChooseWord({'a': 2, 'c': 1, 'b': 1, 't': 1}, wordList, 5)
    print "----------------"
#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    score = 0
    handLength = n
    while handLength > 0:
        # As long as there are still letters left in the hand:
        print "Current Hand: ",
        displayHand(hand) 
        # Display the hand
        wordChosen = compChooseWord(hand, wordList, n) #str(raw_input("Enter word, or a '"'.'"' to indicate that you are finished: "))
        if (wordChosen == None):
            break
        else:
            wordScore = getWordScore(wordChosen, n)
            score = score + wordScore
            print '"' + wordChosen +  '"' + " earned " + str(wordScore) + " points.",
            print "Total: " + str(score) + " points" + "\n"
            # Update the hand
            hand = updateHand(hand, wordChosen)
            handLength = sum(hand.itervalues())
                

    # Game is over 
    print "Total score: " + str(score) + " points."
 
    
    
def testcompPlayHand(wordList):
    #print compPlayHand({'i': 3, 'k': 1, 'd': 1, 'n': 1}, wordList, 6)
    #print "----------------"
    #print compPlayHand({'a': 1, 'd': 2, 'i': 2, 'k': 1, 'o': 1, 'n': 1}, wordList, 8)
    #print "----------------"

    #compPlayHand({'a': 2, 'e': 2, 'i': 2, 'm': 2, 'n': 2, 't': 2}, wordList, 12)
    #print "----------------"
    #compPlayHand({'q': 1}, wordList, 1)
    print "----------------"
    compPlayHand({'a': 1, 'p': 2, 's': 1, 'e': 1, 'l': 1}, wordList, 6)
    print "----------------"
    compPlayHand({'a': 1, 'p': 2, 's': 1, 'e': 1, 'l': 1}, wordList, 8)
    print "----------------"
    #compPlayHand({'a': 2, 'c': 1, 'b': 1, 't': 1}, wordList, 5)
    #print "----------------"   
#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    hand={}
    continuePlaying = True
    while (continuePlaying):
        optionChosen = str.lower(raw_input
                           ("Enter n to deal a new hand, r to replay the last hand, or e to end game: " ))
        if (optionChosen == 'n' or optionChosen == 'r'):
            if (optionChosen == 'r'):
                if (len(hand) ==0):
                    print "You have not played a hand yet. Please play a new hand first!" + "\n"
                    break
                #else:
                    #playHand(hand, wordList, HAND_SIZE)
            choosePlayerType = True
            while (choosePlayerType):
                playerType = str.lower(raw_input
                               ("\n" + "Enter u to have yourself play, c to have the computer play: "))
                #if (optionChosen == 'n' or optionChosen == 'r'):
                if (playerType == 'c' or playerType == 'u'):
                    if (optionChosen == 'n'):
                        hand = dealHand(HAND_SIZE)
                        #playHand(hand, wordList, HAND_SIZE)
                    else:
                        if (len(hand) ==0):
                            print "You have not played a hand yet. Please play a new hand first!" + "\n"
                            break
                    if (playerType == 'c'):
                        compPlayHand(hand, wordList, HAND_SIZE)
                    else:
                        playHand(hand, wordList, HAND_SIZE)
                    choosePlayerType = False
                #else:
                    #playHand(hand, wordList, HAND_SIZE)
        elif (optionChosen == 'e'):
            continuePlaying = False
        else:
            print "Invalid command." + "\n"

  
def testplayGame(wordList):
    playGame(wordList)
    print "YEEOHAO"


def isValidWordinWordList(word, hand):
    wordAsDict = getFrequencyDict(word)  
    for k,v in wordAsDict.iteritems():
        if (hand.get(k, 0) < v):
            return False
    return True
        
            
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    #testcompChooseWord(wordList)
    #testcompPlayHand(wordList)
    testplayGame(wordList)
    #playGame(wordList)


