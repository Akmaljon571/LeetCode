class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        return len(str(int(str(num)[::-1]))) == len(str(num))

test = Solution()
print(test.isSameAfterReversals(num = 1800))
