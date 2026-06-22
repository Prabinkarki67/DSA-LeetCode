class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq_table = {}
        for i in nums:
            if i not in freq_table:
                freq_table[i] = 1
            else:
                return True
        return False