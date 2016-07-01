count=0
strSearchChar='bob'
for i in range(len(s)):
    if (strInput[i-1:i+2] == strSearchChar):
        count+=1
print 'num of ',
print strInput,
print ' = ' + str(count)