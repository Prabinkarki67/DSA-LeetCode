class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        right  = len(num)-1
        while right>=0:
            last = num[right]
            last_int = int(last)
            if last_int %2 == 0 :
                right -= 1
            else:
                return num[0:right+1]
        return ''
        