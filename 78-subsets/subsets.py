class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def getsubset(nums, i, ans, subset):
            if i == len(nums):
                subset.append(ans[:])
                return 

            #Include
            ans.append(nums[i])
            getsubset(nums, i+1, ans, subset)

            #pop last element to go back
            ans.pop()

            #exclude
            getsubset(nums, i+1, ans, subset)





        i = 0
        ans= []
        subset = []
        getsubset(nums, i, ans, subset)
        return subset