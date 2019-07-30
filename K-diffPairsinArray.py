class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        count = []
        dict = {}
        for i in range(len(nums)):
            if nums[i] in dict:
                count.append((dict[nums[i]],nums[i]))
            dict[nums[i]+k] = nums[i]
        return len(set(count))
