def oddTuples(aTuple):
    #returns a new tuple with the odd items from aTuple
    li=[]
    for i in range(0,len(aTuple),2):
        li.append(aTuple[i])

    return tuple(li)

list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
newTup = oddTuples(list)
for i in newTup:
    print i

print(list[0:1])

