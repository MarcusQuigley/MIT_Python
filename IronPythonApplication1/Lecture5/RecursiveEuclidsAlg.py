def gcdRecur(a, b):
#greatest common divisor of two positive integers is 
#the largest integer that divides each of them without remainder 
    if (b == 0):
        return a
    else:
        return gcdRecur(b,(a % b))
    
    """while (b > 0):
        temp = a % b
        a = b
        b = temp
        print temp

    return a"""

print 'gcd = ' +  str(gcdRecur(1071, 462))