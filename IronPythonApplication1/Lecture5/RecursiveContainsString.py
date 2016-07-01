def isIn(char, aStr):
    #true if char is in aStr
    if (len(aStr) == 0):
        return False
    middle = len(aStr)/2
    
    charToCheck = aStr[middle]
    if (charToCheck == char):
        return True
    if (len(aStr) == 1):
        return False

    if (char < charToCheck):
        return isIn(char, aStr[:middle])
    else:
        return isIn(char, aStr[middle:])

print isIn('c', 'abcde')

