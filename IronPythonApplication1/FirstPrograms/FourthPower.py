def square(x):
    return x*x

def fourthPower(x):
    answer=1
    for i in range(4):
       answer = answer * square(x)
    return answer

def fourthPowerBetter(x):
    return square(square(x))

print fourthPower(3)
print fourthPowerBetter(3)
 
