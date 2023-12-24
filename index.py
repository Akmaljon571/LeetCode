class Solution:
    def numIdenticalPairs(self, nums) -> int:
        count = 0
        for i, a in enumerate(nums):
            count += nums[i+1:].count(a)
        return count


test = Solution()
print(test.numIdenticalPairs(nums=[1, 1,1,1]))
