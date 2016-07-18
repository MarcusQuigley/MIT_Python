def swapSort(L): 
    """ L is a list of integers """
    cnt=0
    print "Original L: ", L
    for i in range(len(L)):
        for j in range(len(L)): #(i+1, len(L)):
            if L[j] < L[i]:
                # the next line is a short 
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
                print L
                cnt+=1
    print "Final L: ", L
    print "Count: ", str(cnt)


#swapSort([2,5,23,1,7,21])#,333,6,9, 41, 66, 4344, 3, 632, 65, 78, 64, 3425, 657, 43, 51, 23, 652, 100, 51, 75])

#swapSort([2,5,7, 9, 322, 2444])


'''
Problem 5
'''

def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False

def newsearch(L, e):
    size = len(L)
    for i in range(size):
        if L[size-i-1] == e:
            return True
        if L[i] < e:
            return False
    return False


print search([], 4)
print '--'
print newsearch([], 4)
print '----------------------'
print search([1], 4)
print '--'
print newsearch([1], 4)
print '----------------------'
print search([1], 1)
print '--'
print newsearch([1], 1)
print '----------------------'
print search([1, 2], 4)
print '--'
print newsearch([1, 2], 4)
print '----------------------'
print search([1, 2], 2)
print '--'
print newsearch([1, 2], 2)
print '----------------------'
print search([2,5,23,1,7,21], 4)
print '--'
print newsearch([2,5,23,1,7,21], 4)
print '----------------------'
print search([2,5,23,1,7,21], 23)
print '--'
print newsearch([2,5,23,1,7,21], 23)
print '----------------------'
