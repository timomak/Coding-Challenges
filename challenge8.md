# Is palindrome from firecode
from firecode ([link](https://www.firecode.io/pages/profile/34186))

Problem:
Check is the given string is a palindrome (no string clean up)

Example:
```
is_palindrome("madam") -> True

is_palindrome("aabb") -> False

is_palindrome("race car") -> False

is_palindrome("") -> True
```

My solution:
```Python
def is_palindrome(input_string):
  """
  Runtime: O(n) because of reverse method.
  """
    if input_string == input_string[::-1]: # Reverse String
        return True
    else:
        return False

print(is_palindrome("racecar")) # True
print(is_palindrome("race car")) # False
```
