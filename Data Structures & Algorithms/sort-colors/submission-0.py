class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
         # buckets = [0, 0, 0]
        # for i in nums:
        #     buckets[i] += 1
        
        # i = 0
        # for j in range(len(buckets)):
        #     for _ in range(buckets[j]):
        #         nums[i] = j
        #         i += 1

        i = 0
        left = 0
        right = len(nums) - 1

        while i <= right:
            if nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
                i += 1
            elif nums[i] == 2:
                nums[right], nums[i] = nums[i], nums[right]
                right -= 1
            else:
                i += 1
