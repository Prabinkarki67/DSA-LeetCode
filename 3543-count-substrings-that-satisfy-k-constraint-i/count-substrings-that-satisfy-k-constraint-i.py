class Solution(object):
    def countKConstraintSubstrings(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        s = list(s)
        counter = 0
        for i  in range(1, len(s)+1):
            for j in range(len(s)):
                if j+i > len(s):
                    continue
                num = s[j:j+i]
                ones = num.count('1')
                zeros = num.count('0')
                if ones <= k or zeros <= k:
                    counter +=1 
        return counter   

        