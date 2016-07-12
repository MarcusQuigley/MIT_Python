'''
Write a Python function that returns True if aString is a palindrome (reads the same forwards or reversed) 
and False otherwise. Do not use Python's built-in reverse function or aString[::-1] to reverse strings.
'''

def isPalindrome(aString):
    '''
    aString: a string
    '''
    if (len(aString) < 2): return True
     
    elif (len(aString) == 2):
        return aString[0].lower() == aString[1].lower()
    
    #compare 1st and last. 
    if (aString[0].lower() != aString[-1].lower()):
        return False
     #if true then removif
    return isPalindrome(aString[1:-1])



print isPalindrome('')
