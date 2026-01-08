class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        n=len(digits)
        res = []
        for i in range(n):
            for j in range(n):
                if i==j:
                    continue
                else:
                    for k in range(n):
                        if i == j or j == k or i == k:
                            continue 
                        else:
                            num = digits[i]*100+digits[j]*10+digits[k]
                            if num not in res and num%2 == 0 and num>=100:
                                res.append(num)
        return len(res)