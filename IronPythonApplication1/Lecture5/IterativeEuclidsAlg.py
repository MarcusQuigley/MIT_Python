def gcdIter(a, b):
#greatest common divisor of two positive integers is 
#the largest integer that divides each of them without remainder 
    while (b > 0):
        temp = a % b
        a = b
        b = temp
        print temp

    return a

print 'gcd = ' +  str(gcdIter(462, 1071))