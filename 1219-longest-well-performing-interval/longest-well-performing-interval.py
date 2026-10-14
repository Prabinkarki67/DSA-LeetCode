class Solution(object):
    def longestWPI(self, hours):
        n = len(hours)
        first_index = {}   # prefix value -> earliest index where we saw it
        prefix = 0
        maxm = 0
        
        for j in range(n):
            # update running prefix with this element's +1 / -1
            if hours[j] > 8:
                prefix += 1
            else:
                prefix -= 1
            
            # case 1: the whole prefix from 0..j is positive
            if prefix > 0:
                maxm = j + 1
            
            # case 2: there's an earlier prefix value == prefix - 1
            elif (prefix - 1) in first_index:
                maxm = max(maxm, j - first_index[prefix - 1])
            
            # record the earliest time we've seen this prefix value
            if prefix not in first_index:
                first_index[prefix] = j
        
        return maxm