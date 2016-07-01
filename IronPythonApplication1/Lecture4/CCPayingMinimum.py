def monthlyInterestRate(AnnualRate):
    #Divides the annualRate by 12
    return (AnnualRate / 12)

def minimumMonthlyPayment(monthlyPaymentRate, balance):
    #Multiplies the mPR by balance
    return (monthlyPaymentRate * balance)

def monthlyUnpaidBalance(balance, minMonthlyPayment):
    #Subtracts the mMP from the balance
    return (balance - minMonthlyPayment)

def unpaidBalance(monthlyUnpaidBalance, monthlyInterestRate):
    #multiple the mUB by mIR and then add to mUB
    return (monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance))

def roundStr(floatValue):
    #returns a rounded float as a string
    return str(round(floatValue,2))

balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
totalPaid=0.00
monthlyIntRate = monthlyInterestRate(annualInterestRate)

for i in range(1,13):
    minMonthlyPayment = minimumMonthlyPayment(monthlyPaymentRate, balance)
    totalPaid += minMonthlyPayment
    remainingBalance = monthlyUnpaidBalance(balance, minMonthlyPayment)
    balance = unpaidBalance(remainingBalance, monthlyIntRate)
    #print out results
    print 'Month: ' + str(i)
    print 'Minimum monthly payment: ' + roundStr(minMonthlyPayment)
    print 'Remaining balance: ' + roundStr(balance)

#print totals
print 'Total paid: ' +  roundStr(totalPaid)
print 'Remaining balance: ' + roundStr(balance)



