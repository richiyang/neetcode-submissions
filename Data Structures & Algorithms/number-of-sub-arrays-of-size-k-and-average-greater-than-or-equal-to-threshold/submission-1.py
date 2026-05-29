class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        curSum = 0
        threshold *= k
        for i in range(len(arr)):
            curSum += arr[i]
            if i >= k - 1:
                res += curSum >= threshold
                curSum -= arr[i - k + 1]
        
        return res
