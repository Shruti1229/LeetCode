class Solution:
    def reverse(self, x):
        flag = 0
        sum1 = 0
        if( x < 0 ):
            x = abs(x)
            flag = 1
        
        
        while(x > 0) :
            rem = x % 10 
            sum1 = sum1*10 + rem
            x = x//10
        
        
        
        if(sum1 > pow(2,31)):
            return 0
        else:
            if(flag == 1):
                sum1 = sum1 * -1           
            return sum1
        
