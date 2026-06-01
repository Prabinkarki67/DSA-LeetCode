class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        leng = 0
        temp = ''
        for ch in s:
            if ch not in temp:
                temp += ch
            else:
                leng = max(leng, len(temp))
                idx = temp.index(ch)
                temp = temp[idx + 1:] + ch

        return max(leng, len(temp))