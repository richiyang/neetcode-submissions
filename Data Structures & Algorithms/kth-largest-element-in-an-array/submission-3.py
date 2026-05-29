import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # return heapq.nlargest(k, nums)[-1]

        # minHeap = []
        # heapq.heapify(minHeap)
        # for n in nums:
        #     heapq.heappush(minHeap, n)
        #     if len(minHeap) > k:
        #         heapq.heappop(minHeap)
        #
        # return heapq.heappop(minHeap)

        # nums.sort()
        # return nums[len(nums) - k]

        k = len(nums) - k

        def quickSelect(l, r):
            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]

            if p > k:
                return quickSelect(l, p - 1)
            
            if p < k:
                return quickSelect(p + 1, r)

            return nums[p]
        
        return quickSelect(0, len(nums) - 1)