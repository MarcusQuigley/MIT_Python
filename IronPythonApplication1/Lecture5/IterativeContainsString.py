def isIn(char, aStr):
    #true if char is in aStr
    tempStr = aStr
   # strStart=1
   # strEnd = len(tempStr)
    
   
    while len(tempStr)> 0:
       # print 'S: ' + str(strStart) + ' M: ' + str(middle) + ' E: ' + str(strEnd)
        middle = len(tempStr) // 2
        charToCheck = tempStr[middle-1]
        
        if (charToCheck == char):
            return True
        if (len(tempStr)==1): return False
        #if middle == strStart: break 
        
        if (char < charToCheck):
            tempStr = tempStr[:middle]
        else:
            tempStr = tempStr[middle:]

       # middle = (strStart + strEnd) // 2
        

    return False

print isIn('a', 'abcdef')

