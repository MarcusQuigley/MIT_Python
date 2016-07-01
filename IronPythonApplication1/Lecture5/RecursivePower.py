def recurPower(base, exp):
     #multiply base by exp ie get the power thru multiplication and recursion
     #if exp == 0:
     #    return 1
     if exp == 0:
         base = 1
         return base
     return base * recurPower(base, exp-1)

print (recurPower(3, 1))