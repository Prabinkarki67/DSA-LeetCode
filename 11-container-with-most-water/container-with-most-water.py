class Solution:
    def maxArea(self, height: List[int]) -> int:
        lt= 0
        rt = len(height)-1
        res = 0
        while lt <= rt:
            ht = min(height[lt],height[rt])
            wd = rt - lt
            vol = ht* wd
            res = max(vol, res)
            if height[lt]< height[rt]:
                lt +=1
            else:
                rt -= 1
        return res