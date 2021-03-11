def greatest_common_divisor(n1, n2):
    assert int(n1) == n1 and int(n2) == n2, 'numbers must be integers'
    # euclidean algorithm
    # GCD (48, 18):
    #   48 / 18 --> Dividend: 2; Remainder: 12
    #   18 / 12 --> Dividend: 1; Remainder: 6
    #   12 / 6  --> Dividend: 2; Remainder: 0
    #   ==> 6 is GCD(48, 18)

    # convert any negative numbers
    if n1 < 0:
        n1 = -1 * n1

    if n2 < 0:
        n2 = -1 * n2

    # recurse down for GCD
    if n2 == 0:
        return n1
    else:
        return greatest_common_divisor(n2, n1 % n2)


print(greatest_common_divisor(-15, 40))
print(greatest_common_divisor(18, 40))
print(greatest_common_divisor(5, 13))

