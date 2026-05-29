class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        pre = 1
        post = 1
        r = len(nums) - 1
        for l in range(len(nums)):
            res[l] *= pre
            res[r] *= post
            pre *= nums[l]
            post *= nums[r]
            r -= 1
        return res