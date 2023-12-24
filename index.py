class Solution:
    def search(self, nums, target: int) -> int:
        return nums.index(target) if target in nums else -1


test = Solution()
print(test.search(nums=[-1, 0, 3, 5, 9, 12], target=1))
