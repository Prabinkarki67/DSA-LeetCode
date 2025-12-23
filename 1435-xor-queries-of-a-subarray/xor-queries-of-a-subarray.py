class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)

        #first make xor list seeing the patter as 1^3^4^8
        xor_res = [0]*n 
        xor_res[0] = arr[0]

        for i in range(1, n):
            xor_res[i] = xor_res[i-1] ^ arr[i]

        #now find xor according to qn and store in result
        res = []
        for l, r in queries:
            if l == 0:
                res.append(xor_res[r])
            else:
                res.append(xor_res[r] ^ xor_res[l-1])
        
        return res  