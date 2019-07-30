class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        a = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        lis = []
        s = ""
        str1 = ""
        lis2 = []
        for i in (words):
            lis = [a[ord(j)-97] for j in i]
            str = (s.join(lis))
            if str not in lis2:
                lis2.append(str)
        return len(lis2)
