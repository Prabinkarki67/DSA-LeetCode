class Solution:
    def maxScore(self, s: str) -> int:
        res = []
        n=len(s)-1

        for i in range(n):
            left=''
            right =''
            left = s[0:i+1]
            right = s[i+1:]
            count_left = 0
            count_rt = 0
            for k in range(len(left)):
                if left[k] == '0':
                    count_left += 1
            for k in range(len(right)):
                if right[k] == '1':
                    count_rt += 1
            res.append(count_left+count_rt)
        return max(res)
