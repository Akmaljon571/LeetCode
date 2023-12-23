class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        all_sum = sum(int(e) for e in str(n))
        all_kar = 1
        for a in str(n):
            all_kar *= int(a)
        return all_kar - all_sum


test = Solution()
print(test.subtractProductAndSum(n=234))
