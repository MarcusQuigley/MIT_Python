def applyToEach(L, f):
    #applies the func to the items in the list
    for i in range(len(L)):
        L[i] = f(L[i])

def timesFive(number):
    #returns the number multiplied by 5
    return  (number * 5)


def square(number):
    #returns square of number
    return (number * number)

def plusOne(number):
    #returns number plus 1
    return (number + 1)

testList = [1, -4, 8, -9]
applyToEach(testList, plusOne)
print testList