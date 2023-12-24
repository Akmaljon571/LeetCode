class Solution:
    def sortVowels(self, s: str) -> str:
        unli = 'aeiouAEIOU'
        index = []
        unli_arr = []
        result = [*s]
        for i, a in enumerate(s):
            if a in unli:
                unli_arr.append(a)
                index.append(i)
        unli_arr.sort()
        for i, a in enumerate(unli_arr):
            result[index[i]] = a
        return ''.join(str(i) for i in result)



test = Solution()
print(test.sortVowels(s = "lEetcOde"))
