import math

def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)

def radiationExposureOld(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the 
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.
 
    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to 
      between start and stop times.
    '''
    # FILL IN YOUR CODE HERE...
    totalExposure = 0.0
    count = start
    
    while (count < stop):
        totalExposure +=float(f((count))) * float(step)
        count+=step
 
    return totalExposure

def radiationExposure(start, stop, step):
   
    # This only works online as f function isnt correct
    totalExposure = 0.0
    if (start >= stop):
        return 0
    else:
        totalExposure +=float(f((start))) * float(step)
        return totalExposure + radiationExposure((start+step), stop, step)

 
#print "(0, 4, 0.25)  : " +  str(radiationExposure(0, 4, 0.25))
#print "----------"
#print "(0,5,1)  : " +  str(radiationExposure(0,5,1))
#print "----------"
print "(0, 3, 0.1)  : " +  str(radiationExposure(0, 3, 0.1))
print "----------"
print "(14, 20, 0.1)  : " +  str(radiationExposure(14, 20, 0.1))
print "----------"
 
print '72, 96, 0.4 : ' + str(radiationExposure(72, 96, 0.4))
