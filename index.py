class Solution:
    def shuffle(self, nums, n: int):
        x = nums[:n]
        y = nums[n:]
        result = []
        for i, a in enumerate(x):
            result.append(a)
            result.append(y[i])
        return result

test = Solution()
print(test.shuffle(nums = [2,5,1,3,4,7], n = 3))
