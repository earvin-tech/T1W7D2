def multiply(multiplier):
    return lambda x: x * multiplier

doubler = multiply(2)

tripler = multiply(3)

print(doubler(20))

print(tripler(5))

print(doubler(3))