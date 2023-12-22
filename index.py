# 1108
# class Solution:
#     def defangIPaddr(self, address: str) -> str:
#         return address.replace(".", "[.]")
#
#
# test = Solution()
# print(test.defangIPaddr(address="1.1.1.1"))


# 1920
# class Solution:
#     def buildArray(self, nums):
#         return [nums[a] for a in nums]
#
#
# test = Solution()
# print(test.buildArray(nums=[0, 2, 1, 5, 3, 4]))

# 2011
class Solution:
    def finalValueAfterOperations(self, operations) -> int:
        b = 0
        for a in operations:
            if a == '--X' or a == 'X--':
                b -= 1
            elif a == '++X' or a == 'X++':
                b += 1
        return b


test = Solution()
print(test.finalValueAfterOperations(operations = ["++X","++X","X++"]))
