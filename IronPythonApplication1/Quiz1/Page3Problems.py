stuff  = ["iBoy", "iGirl", "iQ", "iC","iPaid","iPad"]
stuff1 = ("iBoy", "iGirl", "iQ", "iC","iPaid","iPad")
stuff2 = [ ( "iBoy", "iGirl", "iQ", "iC","iPaid","iPad") ]
stuff3 = ( [ "iBoy", "iGirl", "iQ", "iC","iPaid","iPad" ], )
stuff4 = ["iQ"]
stuff5 = "iQ"
 


for thing in stuff:
    if thing == 'iQ':
        print "Found it"

for thing in stuff1:
    if thing == 'iQ':
        print "Found it1"
           
for thing in stuff2:
    if thing == 'iQ':
        print "Found it2"
           
for thing in stuff3:
    if thing == 'iQ':
        print "Found it3"
  
for thing in stuff4:
    if thing == 'iQ':
        print "Found it4"
           
for thing in stuff5:
    if thing == 'iQ':
        print "Found it5"

  
print 'done'

print 'Problem2'

def Square(x):
    return SquareHelper(abs(x), abs(x))

def SquareHelper(n, x):
    if n == 0:
        return 0
    return SquareHelper(n-1, x) + x

print Square(-5)