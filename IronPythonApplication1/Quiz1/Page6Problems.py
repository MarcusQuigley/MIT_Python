'''
Write a function to flatten a list. The list contains other lists, strings, or ints. 
For example, [[1,'a',['cat'],2],[[[3]],'dog'],4,5] is flattened into [1,'a','cat',2,3,'dog',4,5]
'''
def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''

    listCopy = []
    for i in aList:
        if (type(i) == list):
            listCopy.extend(flatten(i))
        else:
            listCopy.append(i)

    return listCopy;

print flatten([1,'a','cat',2,3,'dog',4,5])
print '-------'
print flatten([[1,'a','cat',2],[[[3]],'dog'],4,5])
print '-------'
#print flatten([[1,'a',['cat'],2],[[[3]],'dog'],4,5])
print 'done'