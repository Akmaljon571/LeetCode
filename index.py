class Solution:
    def findFinalValue(self, nums, original: int) -> int:
        while True:
            if original not in nums:
                return original
            original = original * 2

test = Solution()
print(test.findFinalValue(nums = [5,3,6,1,12], original = 3))
