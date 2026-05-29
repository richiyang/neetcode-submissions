class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # L, tot = 0, 0
        # minLen = float("inf")
        # for R in range(len(nums)):
        #     tot += nums[R]
        #     while tot >= target:
        #         minLen = min(minLen, R - L + 1)
        #         tot -= nums[L]
        #         L += 1
            
        # return minLen if minLen != float("inf") else 0

        n = len(nums)
        prefixSum = [0] * (n + 1)
        for i in range(n):
            prefixSum[i + 1] = prefixSum[i] + nums[i]

        res = n + 1
        for i in range(n):
            l, r = i, n
            while l < r:
                mid = (l + r) // 2
                curSum = prefixSum[mid + 1] - prefixSum[i]
                if curSum < target:
                    l = mid + 1
                else:
                    r = mid
            if l != n:
                res = min(res, l - i + 1)
        
        return res % (n + 1)