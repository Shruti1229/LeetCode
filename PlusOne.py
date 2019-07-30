class Solution:
    def plusOne(self, digits):
        
        x = digits[len(digits)-1] 
        if(x==9):
            s = [str(i) for i in digits] 
            res = int("".join(s)) 
            num = res + 1
            num1 = list(map(int, str(num))) 
            digits = num1
        else:
            x = x + 1
            digits[len(digits)-1] = x
        return digits
