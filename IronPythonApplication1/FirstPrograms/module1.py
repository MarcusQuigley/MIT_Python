def item_order (order):
    #counts # of items in order and return "salad:2 hamburger:2 water:1"

    saladCount=0
    burgerCount = 0
    waterCount = 0

    arrItems = order.split(' ')
    for item in arrItems:
       if (item == 'salad'):
           saladCount+=1
       elif (item == 'hamburger'):
             burgerCount+=1
       elif (item == 'water'):
             waterCount+=1

    return 'salad:' + str(saladCount) + ' hamburger:' + str(burgerCount) + ' water:' + str(waterCount)

 



print item_order ('salad water hamburger salad hamburger')
