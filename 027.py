#移除元素



class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        t = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[t] = nums[i]
                t += 1
        return t
