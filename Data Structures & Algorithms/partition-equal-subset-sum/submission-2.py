class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tot = sum(nums)
        if tot % 2:
            return False
        target = tot // 2
        
        # dp = set()
        # dp.add(0)
        
        # for i in range(len(nums) - 1, -1, -1):
        #     nextDP = set()
        #     for t in dp:
        #         if (t + nums[i]) == target:
        #             return True
        #         if (t + nums[i]) < target:
        #             nextDP.add(t + nums[i])
        #         nextDP.add(t)
        #     dp = nextDP
        
        # return False
        dp = [False] * (target + 1)

        dp[0] = True
        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]

        return dp[target]