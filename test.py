def fib(n):
    # fibonacci = [0, 1]
    if n == 0:
        return 0
    if n == 1:
        return 1
    a = 0
    b = 1
    for i in range(0, n - 1):
        c = a + b
        a = b
        b = c
        # fibonacci.append(c)
        if i == (n - 2):
            return c
    # print(fibonacci)

print(fib(10))
