animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

nobody=[]

def biggest(aDict):
    if aDict == None: return None
    if len(aDict) == 0: return None
     
    resultDict = {}
    for k, v in aDict.iteritems():
        if (isinstance(v, list)):
            stripedList =list(v)
            resultDict[k] = len(stripedList)            
        else:
            resultDict[k] = 1
    return max(resultDict, key=resultDict.get) 

print(biggest(animals))


def biggestOLD(aDict):
    if aDict == None: return None
    if len(aDict) == 0: return None
    #import types

    #for item in aList:
    #    #if type(aList[item]) is list:
    #    if isinstance(aList[item], list):# types.ListType):
    #    #if aList[item] is types.TupleType:
    #        traverseList(aList[item])
    #    else:
    #        #if aList[item] is list:
    #        #    traverseList(list(item))
    #        #else:
    #            print item

    #valueCount=0
    '''
    valueCount=0
    for element in aDict:
        if (isinstance(aDict[element], list)):
            valueCount += len(aDict[element])
        else:
            valueCount+=1
    return valueCount 
    '''

    resultDict = {}
    for k, v in aDict.iteritems():
        if (isinstance(v, list)):

            #valueCount = len(aDict[element])
            stripedList =list(v)
            resultDict[k] = len(stripedList)            
        else:
            resultDict[k] = 1
            #valueCount=1
    return max(resultDict, key=resultDict.get) 

print(biggest(animals))
