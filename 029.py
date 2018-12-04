#两数相除



class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        neg = ((dividend < 0) != (divisor < 0))
        dividend = left = abs(dividend)
        divisor = div = abs(divisor)
        t=1
        ans=0
        while left >= divisor:
            left -= div
            ans += t
            t += t
            div += div
            if left < div:
                div = divisor
                t = 1
        if neg:
            return max(-ans, -2**31)
        else:
            return min(ans, 2**31-1)
