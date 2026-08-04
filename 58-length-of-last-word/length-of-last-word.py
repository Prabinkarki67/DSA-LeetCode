class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        a  = s.split()
        if a[-1] == ' ':
            a.remove(-1)
        return len(a[-1])