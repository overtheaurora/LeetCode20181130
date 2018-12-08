#实现strStr()


class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i] != needle[0]:
                continue
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
