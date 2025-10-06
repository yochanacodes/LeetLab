class Solution(object):
    def twoSum(self, nums, target):

        for i in range(len(nums)):
            t = target - nums[i]
            if t in nums and nums.index(t) != i:
                return [i, nums.index(t)]
