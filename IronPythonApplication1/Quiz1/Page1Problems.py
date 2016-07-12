def problem1():
    x="pi"
    y="pie"
    print x
    print y
    return
    print "---------------"
    x,y=y,x
    print x
    print y

def loop(i,j):
    while i >= 0:
        while j >= 0:
            print i, j

def tuples():
    listx = [1, 2, 3]
    tuplex = (1,2,3,listx)
    print listx
    print "---------------"
    print tuplex


def breakLoop():
    for i in range(10):
        if (i==4): 
            break
        print i
    print "breakLoop Done"


problem1()



loop(-1,-1)
print '\n'
#tuples()
print "breakLoop call Start"
breakLoop()
print "breakLoop call finished"
