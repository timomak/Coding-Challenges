# Reverse 2D array
from firecode ([link](https://www.firecode.io/pages/profile/34186))

Problem:
Given a 2D array, reverse the order of the individual array items.

Example:
```
Input => Output
[[1,2,3],[0,0,1]] => [[3,2,1],[1,0,0]]
```

My solution:
```Python
def flip_vertical_axis(matrix):
  """
  Runtime: O(n)
  """
    temp = []
    for array in matrix:
        temp_array = array[::-1] # Reverse items in array
        temp.append(temp_array)
    return temp

print(flip_vertical_axis([[0,0,1], [1,2,3]])) # [[1,0,0], [3,2,1]]
```
