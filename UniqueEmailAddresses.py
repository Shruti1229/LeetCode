class Solution(object):
        
    def numUniqueEmails(self, emails):
        
        lis2 = []
        for stri in emails:
            str1 = []
            a = stri.find('@')
            b = stri.find('+')
            if(b != -1):
                c = b
            else:
                c = a
            
            for i in range(0,c):
                if(stri[i] != '.'):
                    str1.append(stri[i])
                
                
            for i in range(a,len(stri)):
                str1.append(stri[i])
