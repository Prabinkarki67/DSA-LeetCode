class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        count_zero = 0
        count_one = 0
        max_len = 0

        for i in s:
            if i == '0':
                # new zero block starts after ones
                if count_one > 0:
                    count_zero = 0
                    count_one = 0
                count_zero += 1

            else:  # i == '1'
                count_one += 1
            max_len = max(max_len, 2 * min(count_zero, count_one))

        return max_len