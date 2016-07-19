def modten(n):
    print "length: ", str(n)
    result  = n%10
    print "result: ", result
    return result
    #return n%10

 
print "---------------10"
modten(10)
print "---------------3214"
modten(3214)
print "---------------32130200"
modten(32130200)
print "---------------35292399324343"
modten(35292399324343)
print "---------------"
 

#2
def multlist(m, n):
    '''
    m is the multiplication factor
    n is a list.
    '''
    result = []
    for i in range(len(n)):
        result.append(m*n[i])
    return result 

 
print "---------------2, [10]"
print multlist(2, [10])
print "---------------123, [3214, 2,5,23,1,7,21]"
print multlist(123, [3214,2,5,23,1,7,21])
print "---------------32444, [32130200, 2,5,7, 9, 322, 2444, 23,1,7,2145, 664436]"
print multlist(32444, [32130200, 2,5,7, 9, 322, 2444, 23,1,7,2145, 664436])
print "---------------3529239932, 322, 2444, 23,1,7,]"
print multlist(3529239932, [322, 2444, 23,1,7])
print "---------------"


#3
def foo(n):
    print "       in foo: ", n
    if n <= 1:
        return 1
    return foo(n/2) + 1

'''
print "---------------"
print "---------------"
print "---------------10"
foo(10)
print "---------------3214"
foo(3214)
print "---------------32130200"
foo(32130200)
print "---------------35292399324343"
foo(35292399324343)
print "---------------"
'''

#4
def recur(n):
    print "       in recur: ", n
    if n <= 0:
        return 1
    else:
        return n*recur(n-1)
'''
print "---------------"
print "---------------3"
recur(3)
print "---------------15"
recur(15)
print "---------------100"
recur(100)
print "---------------245"
#recur(245)
print "---------------"
'''

def baz(n):
    cnt=0
    for i in range(n):
        for j in range(n):
            #print i,j 
            cnt+=1
    print "n + cnt: ",n,cnt 

'''
print "---------------"
print "---------------3"
baz(3)
print "---------------15"
baz(15)
print "---------------100"
baz(100)
print "---------------245"
baz(245)
print "---------------"
'''



