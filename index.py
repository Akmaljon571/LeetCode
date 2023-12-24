class Solution:
    def entityParser(self, text):
        return text.replace('&quot;', '"').replace('&gt;', '>').replace('&lt;', '<').replace('&apos;', "'").replace(
            '&amp;', '&').replace('&frasl;', '/')


test = Solution()
print(test.entityParser(text="&amp; is an HTML entity but &ambassador; is not."))
