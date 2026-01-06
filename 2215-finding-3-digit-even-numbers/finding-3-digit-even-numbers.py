class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        res = set()
        n = len(digits)

        for i in range(n):
            if digits[i] == 0:      # hundreds place cannot be 0
                continue
            for j in range(n):
                if j == i:
                    continue
                for k in range(n):
                    if k == i or k == j:
                        continue
                    if digits[k] % 2 != 0:   # last digit must be even
                        continue

                    num = digits[i]*100 + digits[j]*10 + digits[k]
                    res.add(num)

        return sorted(res)
