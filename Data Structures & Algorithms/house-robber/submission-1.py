class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        
        nums[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            nums[i] = max(nums[i - 1], nums[i] + nums[i - 2])
        
        return nums[-1]
        # top down
        # memo = [-1] * len(nums)

        # def dfs(i):
        #     if i >= len(nums):
        #         return 0
        #     if memo[i] != -1:
        #         return memo[i]
        #     memo[i] = max(dfs(i + 1), nums[i] + dfs(i + 2))
        
        # return dfs(0)

        # bottom up
        # if not nums:
        #     return 0
        # if len(nums) == 1:
        #     return nums[0]

        # dp = [0] * len(nums)
        # dp[0] = nums[0]
        # dp[1] = max(nums[0], nums[1])

        # for i in range(2, len(nums)):
        #     dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
        
        # return dp[-1]