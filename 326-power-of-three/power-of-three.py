class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def powercalc(n):
            if n==0:
                return 1
            if n==1:
                return 3
            return powercalc(n-1) * powercalc(1)

        if n <=0:
                return False

        for i in range(n):
            power = powercalc(i)
            if power == n:
                return True
            elif power > n:
                return False
        