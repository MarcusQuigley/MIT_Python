def union(set1, set2):
   """
   set1 and set2 are collections of objects, each of which might be empty.
   Each set has no duplicates within itself, but there may be objects that
   are in both sets. Objects are assumed to be of the same type.

   This function returns one set containing all elements from
   both input sets, but with no duplicates.
   """
   newSet=[]
   if len(set1) == 0:
      return set2
   elif set1[0] in set2:
      return union(set1[1:], set2)
   else:
      newSet = set1[0] + union(set1[1:], set2)
      return  newSet


print(union('','abc'))   
print'--------'
print(union('a','abc'))
print'--------'
print(union('ab','abc'))
print'--------'
print(union('d','abc'))
print'--------'
print(union('abc','abc'))
print'--------'

#print(union('','abc'))   
#print'--------'
#print(union('a','abc'))
#print'--------'
#print(union('ab','abc'))
#print'--------'
#print(union('d','abc'))
#print'--------'

#print(union('',''))   
#print'--------'
#print(union('','a'))
#print'--------'
#print(union('','ab'))
#print'--------'
#print(union('a',''))
#print'--------'
#print(union('a','b'))   
#print'--------'
#print(union('c','ab'))
#print'--------'
#print(union('de',''))
#print'--------'
#print(union('ab','c'))
#print'--------'
#print(union('cd','ab'))
#print'--------'