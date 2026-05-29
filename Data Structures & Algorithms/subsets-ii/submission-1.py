class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # def helper(i, nums, currSet, subsets):
        #     if i >= len(nums):
        #         subsets.append(currSet.copy())
        #         return
            
        #     currSet.append(nums[i])
        #     helper(i + 1, nums, currSet, subsets)
        #     currSet.pop()
        #     while i + 1 < len(nums) and nums[i] == nums[i + 1]:
        #         i += 1
        #     helper(i + 1, nums, currSet, subsets)
        
        # nums.sort()
        # currSet, subsets = [], []
        # helper(0, nums, currSet, subsets)
        # return subsets

        # solution 2
        res = []
        nums.sort()
        
        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset[::])
                return
            
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, subset)

        backtrack(0, [])
        return res