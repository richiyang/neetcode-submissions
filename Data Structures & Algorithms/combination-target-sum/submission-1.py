class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # res = []
        # subset = []

        # def dfs(i, cur, tot):
        #     if tot == target:
        #         res.append(cur.copy())
        #         return

        #     if i >= len(nums) or tot > target:
        #         return

        #     cur.append(nums[i])
        #     dfs(i, cur, tot + nums[i])
        #     cur.pop()
        #     dfs(i + 1, cur, tot)

        # dfs(0, [], 0)
        # return res

        # solution 2

        res = []
        nums.sort()

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            
            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    return
                cur.append(nums[j])
                dfs(j, cur, total + nums[j])
                cur.pop()
        
        dfs(0, [], 0)
        return res