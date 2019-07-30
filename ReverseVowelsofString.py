class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        #s = "aA"

        vowels = ['a','e','i','o','u','A','E','I','O','U']
        lis = []
        for i in range(len(s)):
            if s[i] in vowels:
                lis.append(i)
                
        str1 =[i for i in s]
        
        for i in range(len(lis)/2):
            temp = str1[lis[i]]
            str1[lis[i]] = str1[lis[len(lis)-1-i]]
            str1[lis[len(lis)-1-i]] = temp
            
        s1 = ""
        str2 = s1.join(str1)
        return str2
