#Z子形变换



class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        rows = [[] for x in range(numRows)]

        i = 0
        while i < len(s):
            for j in range(numRows):
                if i >= len(s):
                    break
                rows[j].append(s[i])
                i += 1
            for j in range(numRows - 2, 0, -1):
                if i >= len(s):
                    break
                rows[j].append(s[i])
                i += 1

        return ''.join([''.join(row) for row in rows])
