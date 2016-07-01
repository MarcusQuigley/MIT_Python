def monthlyInterestRate(AnnualRate):
    #Divides the annualRate by 12
    return (AnnualRate / 12)

def unpaidBalance(monthlyUnpaidBalance, monthlyInterestRate):
    #multiple the mUB by mIR and then add to mUB
    return (monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance))


balance = 604
annualInterestRate = 0.2
monthlyIntRate = monthlyInterestRate(annualInterestRate)
lowestPayment = 10
total = balance
while total > 0:
    
    #print ' temp Lowest payment: ' + str(lowestPayment)
    for i in range(12):
        total -= lowestPayment
        total = unpaidBalance(total, monthlyIntRate)

    if total > 0:
        lowestPayment += 10
    else: #total=0
        break

    total = balance

print 'Lowest Payment: ' + str(lowestPayment)

 