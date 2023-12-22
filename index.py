class Solution:
    def canBeEqual(self, target, arr) -> bool:
        target.sort()
        arr.sort()
        return target == arr


test = Solution()
print(test.canBeEqual(target = [3,11,9], arr = [3,7,11]))
