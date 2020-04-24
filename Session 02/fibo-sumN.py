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

def fibosum(n):
    res = 0
    for i in range(n +1):
        res = res + fibon(i)
    return res

print("Sum of the first 5 terms of the Fibonacci series: ", fibosum(5))
print("Sum of the first 10 terms of the Fibonacci series: ", fibosum(10))