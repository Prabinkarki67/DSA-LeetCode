class Solution:
    def countLargestGroup(self, n: int) -> int:
        res = [0] * 37

        for i in range(1, n + 1):
            x = i
            sum = 0

            while x != 0:
                sum += x % 10
                x //= 10

            res[sum] += 1

        max_size = max(res)

        count = 0
        for v in res:
            if v == max_size:
                count += 1

        return count
