def twoSum(nums: [int], target: int) -> [int]:
    """
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.

    Runtime: O(n) Two consecutive for loops. dict.get() is Constant time.

    """
    dict = {value: index for index, value in enumerate(nums)}

    for i, v in enumerate(nums):
        new_target = target - v
        if dict.get(new_target) != None:
            if i != dict[new_target]:
                return [i, dict[new_target]]
    return None

print(twoSum(nums = [3,2,4], target = 6)) # [0,1]
