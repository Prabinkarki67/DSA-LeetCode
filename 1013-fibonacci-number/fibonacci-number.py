class Solution:
    def fib(self, n: int) -> int:

        #define basecase as f(0)=0 and f(1) = 1
        if n==0:
            return 0
        elif n==1:
            return 1
        #use recurssion now
        return self.fib(n-1)+self.fib(n-2)





