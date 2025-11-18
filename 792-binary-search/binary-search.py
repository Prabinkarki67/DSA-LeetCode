class Solution:
    def search(self, nums: List[int], tar: int) -> int:
        n=len(nums)
        st = 0
        end = n-1
        while st <= end:
            mid = (st+end)//2
            if nums[mid] == tar:
                return mid
            elif tar > nums[mid]:
                st =mid + 1
            elif tar < nums[mid]:
                end = mid - 1
        return -1