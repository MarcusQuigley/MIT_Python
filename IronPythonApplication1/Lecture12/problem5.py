def genPrimes(): # not working
    number = 2
    lastPrime = 2
    yield number
    while True:
        if ( number % lastPrime     != 0):
            lastPrime = number
            yield number

        number = number + 1

#for n in genPrimes():
#    print n


 

def gen_primes():
    """ Generate an infinite sequence of prime numbers.
    """
    D = {}
    
    # The running integer that's checked for primeness
    q = 2
    
    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            # 
            yield q
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next 
            # multiples of its witnesses to prepare for larger
            # numbers
            # 
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        
        q += 1


for n in gen_primes():
    print n