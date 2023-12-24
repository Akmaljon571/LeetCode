class Solution:
    def findWordsContaining(self, words, x: str):
        arr = []
        for i, a in enumerate(words):
            if x in a:
                arr.append(i)
        return arr

test = Solution()
print(test.findWordsContaining(words = ["leet","code"], x = "e"))
