class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n == 1:
            return nums[0]
        res=[]
        res.append(nums[0])
        res.append(max(nums[0], nums[1]))
        for i in range(2,n):
            maxm = max(res[i-2]+nums[i], res[i-1])
            res.append(maxm)
        return res[n-1]