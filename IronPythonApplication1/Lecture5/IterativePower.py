def iterPower(base, exp):
    #multiply base by exp ie get the power thru multiplication and not **
    result=1
    while exp > 0:
        result *= base
        exp-=1
    return result

print (iterPower(3,4))


    
