def monthlyInterestRate(AnnualRate):
    #Divides the annualRate by 12
    return (AnnualRate / 12)

def unpaidBalance(monthlyUnpaidBalance, monthlyInterestRate):
    #multiple the mUB by mIR and then add to mUB
    return (monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance))

def monthlyLowerBound(balance):
    #divides balance by 12
    return (balance / 12)

def monthlyUpperBound(balance, monthlyInterestRate):
    #if paid in 1 payment we need to calculate the monthly interest compound rate
    return (balance * (1 + monthlyInterestRate)**12)/12.0

def averagePayment(lowestPayment, highestPayment):
    #gets the mid point of the two payments
    return (lowestPayment + highestPayment) / 2
    
def roundStr(floatValue):
    #returns a rounded float as a string
    return str(round(floatValue,2))


balance = 999999

annualInterestRate = 0.18
monthlyIntRate = monthlyInterestRate(annualInterestRate)

lowestPaymentB = monthlyLowerBound(balance)
highestPaymentB = monthlyUpperBound(balance, monthlyIntRate)

lowestPayment = averagePayment(lowestPaymentB, highestPaymentB)
total = balance
while total > 0:
    
    #print ' temp Lowest payment: ' + str(lowestPayment)
    for i in range(12):
        total -= lowestPayment
        total = unpaidBalance(total, monthlyIntRate)

    if abs(total) < 0.01:
        break #we're done

    if total > 0:
        lowestPaymentB = lowestPayment
    elif total < 0:
        highestPaymentB = lowestPayment
    #else: #total=0
     #   break
    lowestPayment = averagePayment(lowestPaymentB, highestPaymentB)
    total = balance

print 'Lowest Payment: ' + roundStr(lowestPayment)

 