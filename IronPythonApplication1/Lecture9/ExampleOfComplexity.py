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
