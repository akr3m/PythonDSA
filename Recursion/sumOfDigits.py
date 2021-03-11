def sumOfDigits(n):
    assert n >= 0 and int(n) == n, 'n must be a positive integer'
    if n < 10:
        return n
    else:
        return sumOfDigits(int(n / 10)) + sumOfDigits(n % 10)


print(sumOfDigits(9))
print(sumOfDigits(13))
print(sumOfDigits(22))
print(sumOfDigits(40))
print(sumOfDigits(1001))
print(sumOfDigits(537))
