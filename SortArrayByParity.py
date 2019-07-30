class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        A1 = [i for i in A if i % 2 == 0 ]
        A2 = [i for i in A if i %2 != 0]
        A1.extend(A2)        
        return A1
