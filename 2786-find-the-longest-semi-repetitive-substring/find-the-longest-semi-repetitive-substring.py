class Solution(object):
    def longestSemiRepetitiveSubstring(self, s):
        if len(s) <= 1:
            return len(s)
        
        i = 0
        repeat = 0
        start = 0
        max_len = 1
        
        while i < len(s):
            j = i + 1
            if j < len(s):
                if s[i] == s[j]:
                    repeat += 1
                
                while repeat > 1:
                    if s[start] == s[start + 1]:
                        repeat -= 1
                    start += 1
                
                max_len = max(max_len, j - start + 1)
            i += 1
        
        return max_len