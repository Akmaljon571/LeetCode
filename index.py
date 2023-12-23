class Solution:
    def prefixCount(self, words, pref: str) -> int:
        count = 0
        for a in words:
            if pref == a[:len(pref)]:
                count += 1
        return count

test = Solution()
print(test.prefixCount(words = ["leetcode","win","loops","success"], pref = "le"))
