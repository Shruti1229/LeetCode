class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count_val = nums.count(val)
        nums.sort()
        s = []
        k = len(nums)
        for j in range(k):
            if(nums[j] == val):
                s.append(j)
        for i in range(len(s)):
            nums[s[i]] = nums[k-1-i]
            
        
        return len(nums)-count_val
