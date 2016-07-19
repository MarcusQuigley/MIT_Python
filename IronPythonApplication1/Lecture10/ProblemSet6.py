#1
def swapSort(L): 
    """ L is a list on integers """
    print "Original L: ", L
    cnt=0
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if L[j] < L[i]:
                # the next line is a short 
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
                #print " swap"
            #print L
            cnt+=1
    print "Final L: ", L
    print "count: ", cnt

print "---------------[3214,2,5,23,1,7,21]"
swapSort([3214,2,5,23,1,7,21])
print "---------------[32130200, 2,5,7, 9, 322, 2444, 23,1,7,2145, 664436]"
swapSort([32130200, 2,5,7, 9, 322, 2444, 23,1,7,2145, 664436])
print "---------------[322, 2444, 23,1,7]"
swapSort([322, 2444, 23,1,7])
#print "---------------35292399324343"
#swapSort(35292399324343)
print "---------------"
 

#2
def modSwapSort(L): 
    """ L is a list on integers """
    print "Original L: ", L
    cnt=0
    for i in range(len(L)):
        for j in range(len(L)):
            if L[j] < L[i]:
                # the next line is a short 
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
                #print L
            cnt+=1
    print "Final L: ", L
    print "count: ", cnt

 
print "---------------[3214,2,5,23,1,7,21]"
modSwapSort([3214,2,5,23,1,7,21])
print "---------------[32130200, 2,5,7, 9, 322, 2444, 23,1,7,2145, 664436]"
modSwapSort([32130200, 2,5,7, 9, 322, 2444, 23,1,7,2145, 664436])
print "---------------[322, 2444, 23,1,7]"
modSwapSort([322, 2444, 23,1,7])
 