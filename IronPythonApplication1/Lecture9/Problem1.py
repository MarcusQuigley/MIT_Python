##import datetime
import time
def linearSearch(L, x):
    for i in L:
        if  i == x:
            return True
    return False


dict={}
start = time.time()
linearSearch([14, 15, 6, 27, 13, 16, 25, 11, 7], 15)
end = time.time()  
dict[0] = (end - start)

start = time.time()
linearSearch([21, 1, 25, 22, 30, 13, 7, 24, 12], 24)
end = time.time()
dict[1] = (end - start)

start = time.time()
linearSearch([20, 10, 1, 7, 4, 22, 25, 12, 31], 20)
end = time.time() 
dict[2] = (end - start)

start = time.time()
linearSearch([9, 3, 12, 24, 7, 8, 23, 11, 19], 8)
end = time.time() 
dict[3] = (end - start)

start = time.time()
linearSearch([4, 12, 20, 17, 9, 14, 7, 24, 6], 7)
end = time.time() 
dict[4] = (end - start)

start = time.time()
linearSearch([13, 9, 22, 3, 10, 17, 11, 2, 12], 26)
end = time.time() 
dict[5] = (end - start)

for k, v in dict.iteritems():
    print 'key ' + str(k) + ','
    print 'value ' + str(v)

    1+1 + (1 + n*3) + (1 + n*3)^2