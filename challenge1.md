# Two-Sum

Problem on LeetCode ([link](https://leetcode.com/problems/two-sum/))

## Task:
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
```
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,

return [0, 1].
```

## My code
First Try:
```Python
class TwoSum:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      """
      Given an array of integers, return indices of the two numbers such that they add up to a specific target.

      Runtime: O(n^2) Double for loop on the array.

      """
        counter = 0 # 1st Index Counter

        for item in nums:
            new_target = target - item # Remainder
            index = 0 # 2nd Index Counter

            for num in nums:
                if num == new_target:
                    return [counter, index]
                index += 1
            counter += 1
        return None


var = TwoSum()
print(var.twoSum(nums = [2, 7, 11, 15], target = 9)) # [0,1]
```
<br>

Second Try:
```Python
def twoSum(nums: [int], target: int) -> [int]:
    """
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.

    Runtime: O(n) Two consecutive for loops. dict.get() is Constant time.

    """
    dict = {value: index for index, value in enumerate(nums)} # {value : index}

    for i, v in enumerate(nums):
        new_target = target - v
        if dict.get(new_target) != None:
            return [i, dict[new_target]]
    return None

print(twoSum(nums = [2, 7, 11, 15], target = 9)) # [0,1]
```
