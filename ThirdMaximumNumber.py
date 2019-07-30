class Solution:
    def thirdMax(self, nums):
        num1 = list(set(nums))
        num1.sort()
        
        if(len(num1) < 3):
            num1 = num1
        
        else:
            num1.pop()
            num1.pop()
        return num1[len(num1)-1]
