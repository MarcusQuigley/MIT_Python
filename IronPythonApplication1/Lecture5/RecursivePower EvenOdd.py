def recurPowerNew (base, exp):
     #multiply base by exp ie get the power thru multiplication and recursion
     if exp == 0:
         return 1
     elif (exp % 2 != 0):
         return base * recurPowerNew (base, exp-1)
     else:
         return recurPowerNew(base*base,exp/2)
         #return (base * recurPowerNew (base, exp) * recurPowerNew (base, exp/2))
      

print (recurPowerNew(3, 4))