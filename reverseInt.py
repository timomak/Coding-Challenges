# Reverse Integer
# Given an integer, reverse its index order
"""
Example 1:
Input: 123
Output: 321

Example 2:
Input: -123
Output: -321

Example 3:
Input: 120
Output: 21
"""
"""
Runtime: O(n * 2)
"""
def reverse_int(n):
    s = str(n)
    a = ""

    for num in s: # O(n)
        if num != 0 and num != "-":
            a = num + a

    # check if the value is negative
    if n < 0:
        a = "-" + a
    return to_string(a)

def to_string(value):
  try:
    return str(int(float(value))) # O(n)
  except:
    return value

print("RETURNED: " + reverse_int(20)) # Should return 2

print("RETURNED: " + reverse_int(123)) # Shoudl return 321

print("RETURNED: " + reverse_int(-456)) # Should return -654 