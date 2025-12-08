class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # Sort using our function
        def diff(person):
            return person[0] - person[1]
        costs.sort(key=diff)
        
        total = 0
        n = len(costs) // 2
        
        # First half → City A
        for i in range(n):
            total += costs[i][0]
        
        # Second half → City B
        for i in range(n, len(costs)):
            total += costs[i][1]
        
        return total
