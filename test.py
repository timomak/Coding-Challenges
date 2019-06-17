class Solution:
    def reverse(self, x: int) -> int:
        if 0 > x:
            x = int("-" + str(x)[:0:-1])
        else:
            x = int(str(x)[::-1])
        if x > 2**31 or x < -2**31:
            return 0
        return x

solution = Solution()
print(solution.reverse(1563847412))
