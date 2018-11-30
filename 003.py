#003 无重复字符的最长子串



class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        maxLen = 0
        usedChar = {}
        for i in range(len(s)):
            if (s[i] in usedChar) and (start<=usedChar[s[i]]):
                start = usedChar[s[i]]+1
            else:
                maxLen = max(maxLen,i-start+1)
            usedChar[s[i]] = i
        return maxLen
