﻿import random 

class Hand(object):
    def __init__(self, n):
        '''
        Initialize a Hand.

        n: integer, the size of the hand.
        '''
        assert type(n) == int
        self.HAND_SIZE = n
        self.VOWELS = 'aeiou'
        self.CONSONANTS = 'bcdfghjklmnpqrstvwxyz'

        # Deal a new hand
        self.dealNewHand()

    def dealNewHand(self):
        '''
        Deals a new hand, and sets the hand attribute to the new hand.
        '''
        # Set self.hand to a new, empty dictionary
        self.hand = {}

        # Build the hand
        numVowels = self.HAND_SIZE / 3
    
        for i in range(numVowels):
            x = self.VOWELS[random.randrange(0,len(self.VOWELS))]
            self.hand[x] = self.hand.get(x, 0) + 1
        
        for i in range(numVowels, self.HAND_SIZE):    
            x = self.CONSONANTS[random.randrange(0,len(self.CONSONANTS))]
            self.hand[x] = self.hand.get(x, 0) + 1
            
    def setDummyHand(self, handString):
        '''
        Allows you to set a dummy hand. Useful for testing your implementation.

        handString: A string of letters you wish to be in the hand. Length of this
        string must be equal to self.HAND_SIZE.

        This method converts sets the hand attribute to a dictionary
        containing the letters of handString.
        '''
        assert len(handString) == self.HAND_SIZE, "Length of handString ({0}) must equal length of HAND_SIZE ({1})".format(len(handString), self.HAND_SIZE)
        self.hand = {}
        for char in handString:
            self.hand[char] = self.hand.get(char, 0) + 1


    def calculateLen(self):
        '''
        Calculate the length of the hand.
        '''
        ans = 0
        for k in self.hand:
            ans += self.hand[k]
        return ans
    
    def __str__(self):
        '''
        Display a string representation of the hand.
        '''
        output = ''
        hand_keys = self.hand.keys()
        hand_keys.sort()
        for letter in hand_keys:
            for j in range(self.hand[letter]):
                output += letter
        return output

    def update(self, word):
        """
        Does not assume that self.hand has all the letters in word.

        Updates the hand: if self.hand does have all the letters to make
        the word, modifies self.hand by using up the letters in the given word.

        Returns True if the word was able to be made with the letter in
        the hand; False otherwise.
        
        word: string
        returns: Boolean (if the word was or was not made)
        """
        # Your code here
        if self.isValidWord(word):
            newHand = self.hand.copy()
            for letter in word:
                newHand[letter] = newHand[letter] -1
            self.hand = newHand
            return True
            #return newHand
        else:
            return False

    def isValidWord(self, wordChosen):
        #if len(wordChosen) > len(self.hand):
        #    return False
        wordList = list(wordChosen)
        hand_keys = self.listOfKeys()# self.hand.keys()
        for letter in wordList:
            try:
                hand_keys.remove(letter)
            except:
                return False
            
        if (self.calculateLen() - len(wordChosen)) <> len(hand_keys):
            return False

        return True

    def listOfKeys(self):
        listKeys=[]
        for letter in self.hand.keys():
            for j in range(self.hand[letter]):
                listKeys.append(letter)
        return listKeys

    
myHand = Hand(7)
print myHand
print myHand.calculateLen()

myHand.setDummyHand('aazzmsp')
print myHand
print myHand.calculateLen()

print myHand.update('try')

print myHand.update('maap')

#print myHand.isValidWord(myHand.hand,'wded')
#print myHand.isValidWord('wded')

print myHand