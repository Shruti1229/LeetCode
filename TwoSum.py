class Solution:
    def twoSum(self, nums, target):
        a = {}
        for i in range(len(nums)):
            if(target - nums[i] not in a):
                a[nums[i]] = i
            else:
                return (a[target-nums[i]],i)        
