def howMany(aDict):
    valueCount=0
    for element in aDict:
        if (isinstance(aDict[element], list)):
            valueCount += len(aDict[element])
        else:
            valueCount+=1
    return valueCount       
    





animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

print howMany(animals)