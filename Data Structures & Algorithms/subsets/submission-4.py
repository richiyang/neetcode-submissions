class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # res = []
        # subset = []

        # def dfs(i):
        #     if i >= len(nums):
        #         res.append(subset.copy())
        #         return
        #     subset.append(nums[i])
        #     dfs(i + 1)
        #     subset.pop()
        #     dfs(i + 1)

        # dfs(0)
        # return res

        # solution 2
        # res = [[]]

        # for num in nums:
        #     res += [subset + [num] for subset in res]
        
        # return res

        #solution 3

        def helper(i, nums, currSet, subsets):
            if i >= len(nums):
                subsets.append(currSet.copy())
                return
            
            currSet.append(nums[i])
            helper(i + 1, nums, currSet, subsets)
            currSet.pop()
            helper(i + 1, nums, currSet, subsets)

        currSet, subsets = [], []
        helper(0, nums, currSet, subsets)
        return subsets

