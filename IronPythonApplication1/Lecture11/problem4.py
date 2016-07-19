class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'

    def __eq__(self, other):
        return (self.getX() == other.getX() and self.getY() == other.getY())

    def __repr__(self):
        return "Coordinate(%d, %d)" % (self.getX(), self.getY())

    #def __repr__(self):
       # return "Fraction(%d, %d)" % (self.numerator, self.denominator)


c = Coordinate(3,4)
t = Coordinate(4,5)
x = Coordinate(3,4)

print c.__eq__(t)
print c.__eq__(x)
print c.__repr__()
print eval(c.__repr__())

