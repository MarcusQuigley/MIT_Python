import string

### DO NOT MODIFY THIS FUNCTION ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print 'Loading word list from file...'
    # inFile: file
    in_file = open(file_name, 'r', 0)
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    print '  ', len(word_list), 'words loaded.'
    in_file.close()
    return word_list

### DO NOT MODIFY THIS FUNCTION ###
def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

### DO NOT MODIFY THIS FUNCTION ###
def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]
        
    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
             
        result={}
        self.alphabet = list(string.ascii_lowercase + string.ascii_uppercase)
 
        rangeLimit = len(self.alphabet)/2
        for i in range(rangeLimit):
            lengthToShift = i + shift
            if lengthToShift > 25:
                lengthToShift = lengthToShift - rangeLimit

            result[self.alphabet[i]]  = self.alphabet[lengthToShift]
            result[self.alphabet[i + rangeLimit]] = self.alphabet[lengthToShift + rangeLimit]
        
        return result

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift

             get codes from 

        '''
 
        messageShifted = []
        shiftDict = self.build_shift_dict(shift)

        for i in range(len(self.message_text)):
            if shiftDict.has_key(self.message_text[i]): #ignore non letters
                messageShifted.append(shiftDict[self.message_text[i]])
            else:
                messageShifted.append(self.message_text[i])
        result = ''.join(messageShifted) 
        return result


class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        Hint: consider using the parent class constructor so less 
        code is repeated
        '''
        Message.__init__(self, text)
        #super(Message,self).__init__(text)
        self.shift = shift
        self.message_text_encrypted = ""
        self.change_shift(self.shift)

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class
        
        Returns: a COPY of self.encrypting_dict
        '''
        return self.encrypting_dict.copy() # set(self.encrypting_dict[:])

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted 

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift (ie. self.encrypting_dict and 
        message_text_encrypted).
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift
        self.encrypting_dict = self.build_shift_dict(self.shift)
        self.message_text_encrypted = self.apply_shift(self.shift)


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        pass #delete this line and replace with your code here
        validWords={}
        for i in range(26):
            shiftedword = self.apply_shift(i)
            if shiftedword in self.valid_words:
                validWords[i] = shiftedword
                #return (i, self.message_text)
                #return (i, shiftedword)
   
        return self.longest_word(validWords)

        #return (shift, decryptedmessage)
    def longest_word(self, dict_validWords):
        if dict_validWords == None or len(dict_validWords) == 0:
            return None
        if len(dict_validWords)   == 1:
            #val = 
            return tuple(dict_validWords.iteritems().next())#, dict_validWords.itervalues().next())
  
        longest_word = ""
        longest_shift = - 1
        for k,v in dict_validWords.iteritems():
            if len(v) > len(longest_word):
                longest_word = v
                longest_shift = k

        if longest_shift != -1:
            return tuple(longest_shift, longest_word)


shift = 2
 
message = Message('hello')
message.build_shift_dict(shift)
print message.apply_shift(shift)
print 'Expected Output: jgnnq'
shift = 6
message = Message('we are taking 6.00.1x')
message.build_shift_dict(shift)
print message.apply_shift(shift)
print 'Expected Output: ks ofs hoywbu 6.00.1l'
shift = 7
message = Message('th!s is Problem Set 6?')
message.build_shift_dict(shift)
print message.apply_shift(shift)
print 'Expected Output: jr ner gnxvat 6.00.1k'

#plaintext = PlaintextMessage('1.hello!!', shift)
#plaintext.change_shift(shift)
#print plaintext.get_encrypting_dict()
#print 'Actual Output:', plaintext.get_message_text_encrypted()

#Example test case (CiphertextMessage)
#ciphertext = CiphertextMessage('jgnnq')
#print 'Expected Output:', (24, 'hello')
#print 'Actual Output:', ciphertext.decrypt_message()


