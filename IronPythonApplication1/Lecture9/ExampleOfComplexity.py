def f(x):
    for i in range(1000): #1000 - Constant
         ans = i
    for i in range(x):  # 2x - Linear
        ans += 1
    for i in range(x):  # 2x squared  - Polynomial. Also known as Quadratic. Nested loops or recursive func calls
         for j in range(x):
            ans += 1


#Complexity	is	1000	+	2x	+	2x2,	if	each	line	takes	one	step	

def genExponentialComplexity(L):
    res = []
    if len(L) == 0:
        return [[]]
    smaller = genExponentialComplexity(L[:-1]) # go thru all but last element
    extra = L[-1:] # get last element
    new = []
    for small in smaller:
        new.append(small + extra)
    return smaller + new


print genExponentialComplexity([1,2])

def LogdefnIntToString(i):  # - Log n
    digits = '0123456789'
    if i == 0:
        return 0
    result = ''
    while i > 0:
        result = digits[i%10] + result #strip off last digit of i
        i = i/10                        # divide i by 10 ie remove last digit
    return result


print LogdefnIntToString(304203)
