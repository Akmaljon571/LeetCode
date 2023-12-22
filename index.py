class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")


test = Solution()
print(test.defangIPaddr(address="1.1.1.1"))
