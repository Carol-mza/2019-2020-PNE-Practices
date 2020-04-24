def fibon(n):
    if n in [0, 1]:
        return n
    n1 = 0
    n2 = 1
    for i in range(2, n+1):
        term = n1 + n2
        n1 = n2
        n2 = term
    return term

print("5th Fibonacci therm: ", fibon(5))
print("10th Fibonacci therm: ", fibon(10))
print("15th Fibonacci therm: ", fibon(15))