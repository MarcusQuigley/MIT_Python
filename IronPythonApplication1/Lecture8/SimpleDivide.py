def SimpleDivide(item, denom):
    try:
        return item/denom
    except ZeroDivisionError, e:
        return 0


   
def FancyDivide(list_of_numbers, index):
   assert not len(list_of_numbers) ==0, 'grades are empty'
   denom = list_of_numbers[index]
   return [SimpleDivide(item, denom)
               for item in list_of_numbers]



list = FancyDivide([0, 2, 4], 0)
print list