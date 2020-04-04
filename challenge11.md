# IsPalindrome

```Python
# Is Palindrome
# Input: Taco cat
# Output: True

"""
Set a start and end index values

as long as start value doesnt equal end value
    copare the two values

        if identical: 
            continue

        if not identical:
            stop
        
        change the two orinal values

return true

"""

"""
Runtime: O(n / 2)
"""
def is_palindrome(string):
    palindrome = list(string.lower())
    # Set a start and end index values
    start = 0
    end = len(palindrome) - 1

    print("list: ",palindrome)
    # as long as start value doesn't equal end value
    while end > start:
        # copare the two values
        print("Start: {}\nEnd:{}".format(start, end))
        # if not identical values at list index
        if palindrome[start] != palindrome[end]:
            return False
        start += 1
        end =- 1

    return True

print(is_palindrome('Tacocat'))

```