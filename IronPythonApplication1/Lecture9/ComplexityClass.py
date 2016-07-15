def LogdefnIntToString(i):
    digits = '0123456789'
    if i == 0:
        return 0
    result = ''
    while i > 0:
        result = digits[i%10] + result #strip off last digit of i
        i = i/10                        # divide i by 10 ie remove last digit
    return result


print LogdefnIntToString(304203)