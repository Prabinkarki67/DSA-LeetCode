class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        sum = 0 
        left = 0
        right = len(piles)-2

        while left <= right:
            sum+= piles[right]
            left += 1
            right -= 2
        return sum