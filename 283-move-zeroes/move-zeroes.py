class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lt = 0
        rt = 0
        while rt < len(nums):
            if nums[lt]==0 and nums[rt] != 0:
                nums[lt], nums[rt] = nums[rt], nums[lt]
                lt+=1
                rt+=1
            elif nums[lt]!=0 and nums[rt] == 0:
                lt+=1
                rt+=1
            elif nums[lt]!=0 and nums[rt] != 0:
                lt+=1
                rt+=1
            else:
                rt+=1