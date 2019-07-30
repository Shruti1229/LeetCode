class Solution:
    def hammingDistance(self, x, y):
        count = 0
        xor = x ^ y
        binary_y = "{0:b}".format(xor)
        
        x_b = [int(i) for i in binary_y]
        #print(x_b)
        for i in range(len(x_b)):
            if x_b[i] == 1 :
                count = count + 1
        return count
