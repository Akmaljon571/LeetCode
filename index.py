class Solution:
    def arrangeWords(self, text: str) -> str:
        result = {}
        for i, a in enumerate(text.split()):
            result[i] = len(a)
        sort = sorted(result, key=result.get)
        return ' '.join([str(text.split()[a]) for a in sort]).capitalize()


test = Solution()
print(test.arrangeWords(text="Is leetcode cool"))
