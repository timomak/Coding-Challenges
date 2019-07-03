# Fibonacci from firecode
from firecode ([link](https://www.firecode.io/pages/profile/34186))

Problem:
Create a fibonacci function.

Example:
```

```

My solution:
```Python
def fib(n):
  """
  Runtime: O(n)
  Commented out code if you need an array of all fibonacci.
  """
    # fibonacci = [0, 1]
    if n == 0: # In case the input is 0
        return 0
    if n == 1: # In case the input is 1
        return 1
    a = 0
    b = 1
    for i in range(0, n - 1): # O(n)
        c = a + b
        a = b
        b = c
        # fibonacci.append(c)
        if i == (n - 2): # Because we added the first two items manually.
            return c
    # print(fibonacci)

print(fib(10)) # 55
```
