class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lis1 = []
        lis2 = []
        mul = 1
        nums1 = [i for i in nums if i >= 0]
        nums2 = [-1*i for i in nums if i < 0 ]
        
        if(len(nums1) > 2):
            if(len(nums2) < 2):
                a = max(nums1)
                index1 = nums1.index(a)
                del nums1[index1]

                b = max(nums1)
                index2 = nums1.index(b)
                del nums1[index2]

                c = max(nums1)
                #print("a")
            else:
                a = max(nums1)
                index1 = nums1.index(a)
                del nums1[index1]

                b = max(nums1)
                index2 = nums1.index(b)
                del nums1[index2]
                c = max(nums1)
                
                d = max(nums2)
                index4 = nums2.index(d)
                del nums2[index4]
                e = max(nums2)
                lis1.extend([a,b,c])
                lis2.extend([d,e])
                if(b*c > d*e):
                    b = b
                    c = c
                else:
                    b = d
                    c = e
                
                #print("b")
                
                
        
        elif(len(nums1)>=1 and len(nums1)<2):
            a = nums1[0]
            b = max(nums2)
            index4 = nums2.index(b)
            del nums2[index4]
            c = max(nums2)
            #print("c")
        else:
            a = max(nums2)
            index1 = nums2.index(a)
            del nums2[index1]
            b = max(nums2)
            index2 = nums2.index(b)
            del nums2[index2]
            c = max(nums2)
            mul = mul*-1
            #print("d")
        mul = mul * a*b*c
        
        return mul
