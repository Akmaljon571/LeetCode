# class Solution:
#     def defangIPaddr(self, address: str) -> str:
#         return address.replace(".", "[.]")
#
#
# test = Solution()
# print(test.defangIPaddr(address="1.1.1.1"))


class Solution:
    def buildArray(self, nums):
        return [nums[a] for a in nums]


test = Solution()
print(test.buildArray(nums=[0, 2, 1, 5, 3, 4]))
