class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        x =(int(a,2))
        y = (int(b,2))
        z = x + y
        #print(bin(z))
        #print("{0:b}".format(z))
        return str("{0:b}".format(z))
