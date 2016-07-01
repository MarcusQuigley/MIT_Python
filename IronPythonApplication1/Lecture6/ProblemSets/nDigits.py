def ndigits(x):
    if (x == 0) : return 0
    absX = abs(x)
    digitsStr = str(absX)
    if (len(digitsStr)) == 1:
        return 1
    return 1 + ndigits(int(digitsStr[:(len(digitsStr)-1)]))
    #return 1 + ndigits(int(digitsStr[1:]))

print ndigits(-2279044)
print "-------"
print ndigits(234)
print "-------"
print ndigits(1)
print "-------"
print ndigits(0)
print "-------"

def FancyDivide(numbers,index):
    try:
        denom = numbers[index]
        for i in range(len(numbers)):
            numbers[i] /= denom
    except IndexError, e:
        print "-1"
    else:
        print "1"
    finally:
        print "0"

FancyDivide([0, 2, 4], 0)