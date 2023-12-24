class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return (t*2)+num

test = Solution()
print(test.theMaximumAchievableX(num = 4, t = 1))
