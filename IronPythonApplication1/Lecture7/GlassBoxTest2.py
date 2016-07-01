def foo(x, a):
   """
   x: a positive integer argument
   a: a positive integer argument

   returns an integer
   """
   count = 0
   while x >= a:
      count += 1
      x = x - a
   return count


print(foo(2,5))   
print'--------'
print(foo(5,6))
print'--------'
print(foo(9,7))
print'--------'

print(foo(10,3))
print'--------'
print(foo(1,4))
print'--------'
print(foo(10,6))
print'--------'

print(foo(100,5))
print'--------'
print(foo(96,5))
print'--------'
print(foo(22,5))
print'--------'

 