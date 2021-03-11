def power_of_number(x, n):
    assert n >= 0 and int(n) == n, 'n must be a positive number'

    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        return x * power_of_number(x, n-1)


print(power_of_number(2, 2))
print(power_of_number(2, 3))
print(power_of_number(2, 4))
print(power_of_number(2, 1))
print(power_of_number(2, 0))
# print(power_of_number(2, -1))
