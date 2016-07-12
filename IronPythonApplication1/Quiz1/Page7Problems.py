'''
Write a function called dict_interdiff that takes in two dictionaries (d1 and d2). 
The function will return a tuple of two dictionaries: a dictionary of the intersect of d1 and d2 
and a dictionary of the difference of d1 and d2, calculated as follows:
'''


def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''

    # symmetric difference, keys in either d1 or d2 but not both.
    sym_diff = d1.viewkeys() ^ d2
    # intersection, keys that are common to both d1 and d2.
    intersect = d1.viewkeys() & d2
    # apply f on values of the keys that common to both dicts.
    a = {k: f(d1[k], d2[k]) for k in intersect}
    b = {k: d1[k] for k in sym_diff & d1.viewkeys()}
    # add key/value pairings from d2 using keys that appear in sym_diff 
    b.update({k: d2[k] for k in sym_diff & d2.viewkeys()})
    return a,b

def f(a,b):
    return a+b

d1 = {1:30, 2:20, 3:30, 5:80}
d2 = {1:40, 2:50, 3:60, 4:70, 6:90}

print dict_interdiff(d1, d2)