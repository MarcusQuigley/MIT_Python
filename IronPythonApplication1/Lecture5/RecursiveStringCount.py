def lenRecur(aStr):
    #count length of string recursively
    count=0
    if (aStr == ''):
        return count
    count=1
    return count + lenRecur(aStr[:-1])
     

print lenRecur('marcus')