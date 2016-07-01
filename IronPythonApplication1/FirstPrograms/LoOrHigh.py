def clip(lo, x, hi):
    if (x < lo):
        return lo
    if (x > hi):
        return hi
    else:
        return x




def clip2(lo, x, hi):
    #without conditionals
     return min(hi,max(x, lo))
    
print clip2(4,2,1)