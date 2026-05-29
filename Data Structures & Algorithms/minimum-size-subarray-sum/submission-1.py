class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L, tot = 0, 0
        minLen = float("inf")
        for R in range(len(nums)):
            tot += nums[R]
            while tot >= target:
                minLen = min(minLen, R - L + 1)
                tot -= nums[L]
                L += 1
            
        return minLen if minLen != float("inf") else 0