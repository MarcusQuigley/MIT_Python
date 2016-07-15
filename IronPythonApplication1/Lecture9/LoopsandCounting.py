def countForLoop(x):
    #unfor needs to be done using f11
    total = 0
    for i in range(x):
        total+=1
    return total

print countForLoop(2)
print countForLoop(0)


def countForLoopInSet(x):
    #unfor needs to be done using f11
    total = 0
    for i in x:
        total+=1
    return total

print countForLoopInSet([2,3])
print countForLoopInSet([])