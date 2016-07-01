balance = 1234.56
annualInterestRate = 12.25
monthlyPaymentRate = 200.23

for i in range(12):
    monthlyInterestRate = annualInterestRate/12
    monthlyPayment = monthlyPaymentRate * monthlyInterestRate
    balance = balance-monthlyPayment


