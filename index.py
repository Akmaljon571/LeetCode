class Solution:
    def capitalizeTitle(self, title: str) -> str:
        return ' '.join(a.capitalize() if len(a) > 2 else a.lower() for a in title.split())

test = Solution()
print(test.capitalizeTitle(title = "capiTalIze tHe titLe"))
