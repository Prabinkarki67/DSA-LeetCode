class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def pow_calc(x, n):
            if n == 0:
                return 1
            #for big n, make n half and find power of half n   and multiply with itself for faster approach
            half = pow_calc(x, n // 2)

            if n % 2 == 0:
                return half * half
            else:
                return half * half * x
           

        if n>=0:
            return pow_calc(x,n)
        else:
            return 1/pow_calc(x, -1*n)