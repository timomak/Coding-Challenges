# Leap from Exercism
from Exercism ([link](https://exercism.io/my/solutions/d6308055bd3f4e7ea1182db9086ee708))

Problem:
Given a year, return a bool if it's a leap year.
```
on every year that is evenly divisible by 4
  except every year that is evenly divisible by 100
    unless the year is also evenly divisible by 400
```


Example:
```
2000 => True
1970 => False
```

My solution:
```Python
def leap_year(year):
    if (year % 4) == 0:

        divisible_by_100 = (year % 100) == 0
        # print("Hundred:" ,divisible_by_100, (year % 100) )

        divisible_by_400 = (year % 400) == 0
        # print("four hunndred:", divisible_by_400, (year % 400) )

        if divisible_by_100 == True:
            if divisible_by_400 == True:
                # print("Divisible by 400 and 100")
                return True
            else:
                # print("Divisible by 100")
                return False
        # print("Divisible by 4")
        return True
    # print("Not a leap year")
    return False

print(leap_year(1996)) # True
```
