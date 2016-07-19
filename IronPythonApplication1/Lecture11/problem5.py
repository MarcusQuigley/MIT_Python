class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def intersect(self, other):
        setSelf = set(self.vals)
        setOther = set(other.vals) 
        result = setSelf.intersection(setOther)
        intSetResult=intSet()
        for e in result:
            intSetResult.insert(e)
        return intSetResult
        #return list(setSelf.intersection(setOther))

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'

    def __len__(other):
         return len(other.vals)

    def __nonzero__(self):
        if self.vals is None:
            return False
        return self.vals.count > 0



setA = intSet()
setA.insert(-20)
setA.insert(-19)
setA.insert(-9)
setA.insert(-4)
setA.insert(1)
setA.insert(2)
setA.insert(5)
setA.insert(13)
setA.insert(20)

x = len(setA)
print x


setB = intSet()
setB.insert(-16)
setB.insert(-11)
setB.insert(-6)
setB.insert(-2)
setB.insert(-1)
setB.insert(6)
setB.insert(7)
setB.insert(14)
setB.insert(203)

yy = setA.intersect(setB)
print yy

setC = intSet()
setD = intSet()

print setC.intersect(setD)

print len(setC)

'''
setA: {-20,-19,-9,-4,-1,2,5,13,20}
len(setA):

setA: {}
len(setA):

'''