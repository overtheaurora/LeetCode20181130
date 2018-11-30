#最长回文子串


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        result = ""
        for i in range(length):
            left = i
            right = i
            while left>0 and right<length-1 and s[left-1]==s[right+1]:
                left-=1
                right+=1
            if right-left+1>len(result):
                result = s[left:right+1]
        for i in range(length-1):
            if s[i] == s[i+1]:
                right = i+1
                left = i
                while left>0 and right<length-1 and s[left-1]==s[right+1]:
                    left-=1
                    right+=1
                if right-left+1>len(result):
                    result = s[left:right+1]
        return result
