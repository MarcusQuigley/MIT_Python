def test(x):
    print x
    total=0
    while x > 0:
        x /= 2
        total += x
        print x

def test2(x):
     cnt=0
     total=0
     while x > 0:
        x -= 1
        total += x
        cnt+=1
     return cnt

'''
test(100)
print '-------'
test(1000)
print '-------'
test(10)
print '-------'
test(97)
'''
print test2(100)
print '-------'
print test2(834)
