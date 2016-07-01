import math

def areaPolygon(n, s):
    top = 0.25 * n * (s*s)
    btm = math.tan(math.pi/n)
    return top/btm

def perimeterPolygon(n, s):
    return ((n*s) **2)

def polysum(n, s):
    total = areaPolygon(n, s) +  perimeterPolygon(n, s)
    return round(total, 4)


print polysum(4,5)