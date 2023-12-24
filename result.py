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


# 2114
# class Solution:
#     def mostWordsFound(self, sentences) -> int:
#         count = 0
#         for a in sentences:
#             if count < len(a.split()):
#                 count = len(a.split())
#         return count


# 2119
# class Solution:
#     def isSameAfterReversals(self, num: int) -> bool:
#         return len(str(int(str(num)[::-1]))) == len(str(num))


# 2129
# class Solution:
#     def capitalizeTitle(self, title: str) -> str:
#         return ' '.join(a.capitalize() if len(a) > 2 else a.lower() for a in title.split())


# 2154
# class Solution:
#     def findFinalValue(self, nums, original: int) -> int:
#         while True:
#             if original not in nums:
#                 return original
#             original = original * 2


# 2185
# class Solution:
#     def prefixCount(self, words: List[str], pref: str) -> int:
#         count = 0
#         for a in words:
#             if pref == a[:len(pref)]:
#                 count += 1
#         return count


# 1281
# class Solution:
#     def subtractProductAndSum(self, n: int) -> int:
#         all_sum = sum(int(e) for e in str(n))
#         all_kar = 1
#         for a in str(n):
#             all_kar *= int(a)
#         return all_kar - all_sum


# 1287
# class Solution:
#     def findSpecialInteger(self, arr) -> int:
#         result = {}
#         for a in arr:
#             if a not in result:
#                 result[a] = arr.count(a)
#         return max(result, key=result.get)


# 704
# class Solution:
#     def search(self, nums, target: int) -> int:
#         return nums.index(target) if target in nums else -1


# 709
# class Solution:
#     def toLowerCase(self, s: str) -> str:
#         return s.lower()


# 2235
# class Solution:
#     def sum(self, num1: int, num2: int) -> int:
#         return num1 + num2

# 1512
# class Solution:
#     def numIdenticalPairs(self, nums) -> int:
#         count = 0
#         for i, a in enumerate(nums):
#             count += nums[i+1:].count(a)
#         return count


# 2769
# class Solution:
#     def theMaximumAchievableX(self, num: int, t: int) -> int:
#         return (t*2)+num


# 2942
# class Solution:
#     def findWordsContaining(self, words, x: str):
#         arr = []
#         for i, a in enumerate(words):
#             if x in a:
#                 arr.append(i)
#         return arr


# 1470
# class Solution:
#     def shuffle(self, nums, n: int):
#         x = nums[:n]
#         y = nums[n:]
#         result = []
#         for i, a in enumerate(x):
#             result.append(a)
#             result.append(y[i])
#         return result


# 2545
# class Solution:
#     def sortTheStudents(self, score, k: int):
#         return sorted(score, key=lambda x: x[k], reverse=True)


# 1410
# class Solution:
#     def entityParser(self, text):
#         return text.replace('&quot;', '"').replace('&gt;', '>').replace('&lt;', '<').replace('&apos;', "'").replace('&amp;', '&').replace('&frasl;', '/')
