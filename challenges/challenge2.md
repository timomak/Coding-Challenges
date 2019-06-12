# Reverse Integer
Problem on Leetcode ([link](https://leetcode.com/problems/reverse-integer/))

## Task:
> Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
```
Input: 123
Output: 321
```

Example 2:
```
Input: -123
Output: -321
```

Example 3:
```
Input: 120
Output: 21
```
### Note:
> Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

## My Code

```Python
class Solution:
    def reverse(self, x: int) -> int:
        if 0 > x:
            x = int("-" + str(x)[:0:-1])
        else:
            x = int(str(x)[::-1])
        if x > 2**31 or x < -2**31:
            return 0
        return x
```

> I decided to reverse the string.

I began with the plan of reversing the string.

Quickly accomplished the task but it didn't work for the minus sign being displayed at the opposite side of the string. It needed to be an integer and follow the expected output like in the examples.

I decided to remove the string if the integer was negative and add it back after the string was reversed and then return it as an integer.

The last requirement was solved by adding a conditional to make sure it returns **0** if the int is larger than 32-bit.
