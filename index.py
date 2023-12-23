class Solution:
    def findSpecialInteger(self, arr) -> int:
        result = {}
        for a in arr:
            if a not in result:
                result[a] = arr.count(a)
        return max(result, key=result.get)

test = Solution()
print(test.findSpecialInteger(arr = [1,2,2,6,6,6,6,7,10]))
