def selSort(L):
    for i in range(len(L)-1):
        minIdx=i
        minVal = L[i]
        j=i+1
        while j < len(L):
            if minVal > L[j]:
                minIdx = j
                minVal = L[j]
            j += 1
        if minIdx != i:
            temp = L[i]
            L[i] = L[minIdx]
            L[minIdx] = temp

def newSort(L):
    for i in range(len(L) - 1):
        j = i + 1
        while j < len(L):
            if L[i] > L[j]:
                temp = L[i]
                L[i] = L[j]
                L[j] = temp
            j += 1



