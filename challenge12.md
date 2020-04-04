# Check Permutation

```Python
# Check permutation
# is the string an alteration or reorder of the other?

# Taco = oaTc === True

"""
create a ductionary

for each letter of the first string
    create a key in the dict, set the value as an int if it doesn't exist

    if it exists already, add to it

run through the second string, and do the same but subtract
    if the value is already 0, return false

return true

"""
"""
Runtime: O(n * 2)
"""
def check_permutation(string1, string2): 
    # create a ductionary
    letter_count = dict()

    # for each letter of the first string
    for letter in string1:
        print("Letter: ", letter)
        # print("Dict Value: ", letter_count[letter])
    #     create a key in the dict, set the value as an int if it doesn't exist
        if bool(letter_count.get(letter)) == False:
            letter_count[letter] = 1
        else:
            letter_count[letter] += 1

    for letter in string2:
    # create a key in the dict, set the value as an int if it doesn't exist
        if bool(letter_count.get(letter)) == False:
            return False
        elif letter_count[letter] == 0:
            return False
        else:
            letter_count[letter] -= 1
       
    return True

print(check_permutation('tatco', 'octta'))
```