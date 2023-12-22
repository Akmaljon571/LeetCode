# 1108
# class Solution:
#     def defangIPaddr(self, address: str) -> str:
#         return address.replace(".", "[.]")


# 1920
# class Solution:
#     def buildArray(self, nums):
#         return [nums[a] for a in nums]
#
#


# 2011
# class Solution:
#     def finalValueAfterOperations(self, operations) -> int:
#         b = 0
#         for a in operations:
#             if '--' in a:
#                 b -= 1
#                 continue
#             b += 1
#         return b


# 1446
# class Solution:
#     def maxPower(self, s: str) -> int:
#         count = {}
#         for i, a in enumerate(s):
#             if i != len(s)-1:
#                 if s[i+1] == a:
#                     if a not in count:
#                         count[a] = 2
#                         continue
#                     count[a] += 1
#                 elif a in count and s[i+1] != a:
#                     count[i] = count[a]
#                     del count[a]
#         return max(count.values()) if count != {} else 1


# 1451
# class Solution:
#     def arrangeWords(self, text: str) -> str:
#         result = {}
#         for i, a in enumerate(text.split()):
#             result[i] = len(a)
#         sort = sorted(result, key=result.get)
#         return ' '.join([str(text.split()[a]) for a in sort]).capitalize()


# 1455
# class Solution:
#     def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
#         for i, a in enumerate(sentence.split(), start=1):
#             if a.startswith(searchWord):
#                 return i
#         return -1


# 1480
# class Solution:
#     def runningSum(self, nums):
#         arr = [0]
#         for e in nums:
#             arr.append(arr[-1]+e)
#         arr.pop(0)
#         return arr


# 1460
# class Solution:
#     def canBeEqual(self, target, arr) -> bool:
#         target.sort()
#         arr.sort()
#         return target == arr