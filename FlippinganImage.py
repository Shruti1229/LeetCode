class Solution:
    def flipAndInvertImage(self, A):
    
        flip_image = []
        temp = []
        for i in range(len(A)):
            flip = [1 if x==0 else 0 for x in A[i]]
            temp.append(flip)
        
        for i in range(len(temp)):
            B = temp[i]
            
            B.reverse()
            flip_image.append(B)
        
        
        #print(A[0].reverse())
        return flip_image
