def fibonacci(n):
    assert n >= 0 and int(n) == n, 'n must be a positive integer'

    if (n <= 1):
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))
print(fibonacci(6))
print(fibonacci(7))
print(fibonacci(8))
print(fibonacci(9))
print(fibonacci(10))
print(fibonacci(11))
print(fibonacci(12))
print(fibonacci(13))
print(fibonacci(14))
