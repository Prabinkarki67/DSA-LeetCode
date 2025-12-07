class Solution:
    def getSmallestString(self, s: str) -> str:
        arr = list(s)
        n = len(arr)
        rt = 0
        left = 1
        while left < n:
            if arr[rt] > arr[left] and (int(arr[rt]) % 2 == int(arr[left]) % 2):
                arr[rt], arr[left] = arr[left], arr[rt]
                return "".join(arr)
            rt += 1
            left += 1
        return s