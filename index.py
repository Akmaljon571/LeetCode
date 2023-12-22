class Solution:
    def superPow(self, a: int, b) -> int:
        for e in b:
            print(a ** e)
        return 1

test = Solution()
print(test.superPow(a = 1, b = [4,3,3,8,5,2]))
