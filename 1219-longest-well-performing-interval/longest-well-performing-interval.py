class Solution(object):
    def longestWPI(self, hours):
        n = len(hours)
        first_index = {}   
        prefix = 0
        maxm = 0
        
        for j in range(n):

            if hours[j] > 8:
                prefix += 1
            else:
                prefix -= 1
            
            if prefix > 0:
                maxm = j + 1
            

            elif (prefix - 1) in first_index:
                maxm = max(maxm, j - first_index[prefix - 1])
            

            if prefix not in first_index:
                first_index[prefix] = j
        
        return maxm