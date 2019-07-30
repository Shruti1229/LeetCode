class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        l = len(s)//2
        for i in range(0,l):
            
            temp = s[i]
            s[i] = s[len(s)-i-1]
            s[len(s)-i-1] = temp
