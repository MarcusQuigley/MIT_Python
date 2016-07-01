def maxOfThree(a,b,c) :
    """
    a, b, and c are numbers

    returns: the maximum of a, b, and c        
    """
    if a > b:
        bigger = a

    else:
        bigger = b

    if c > bigger:
        bigger = c

    return bigger

 
#print(maxOfThree(2, -10, 100))  #Commented section is the answer
#print'--------'
#print(maxOfThree(7, 9, 10))
#print'--------'
#print(maxOfThree(6, 1, 5))
#print'--------'
#print(maxOfThree(0, 40, 20))
#print'--------'

print(maxOfThree(10, 100, -20))
print'--------'
print(maxOfThree(99, 0, 20))
print'--------'
print(maxOfThree(1, 60, 300))
print'--------'
 