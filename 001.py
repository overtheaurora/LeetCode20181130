#001.两数之和




class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        re_dic = {}
        for i in range(len(nums)):
            if nums[i] in re_dic:
                return [re_dic[nums[i]],i]
            else:
                re_dic[target-nums[i]] = i
