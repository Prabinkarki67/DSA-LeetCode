class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curr = 0
        has = {0: 1}
        ans = 0

        for i in nums:
            curr += i

            num = curr - k

            if num in has:
                ans += has[num]

            if curr in has:
                has[curr] += 1
            else:
                has[curr] = 1
        return ans