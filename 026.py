#删除排序数组中的重复项


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        j=0
        for i in range(1,len(nums)):
            if nums[j] != nums[i]:
                j+=1
                nums[j]=nums[i]
        return j+1
