class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        curSum = 0
        L = 0
        for i in range(len(arr)):
            curSum += arr[i]
            if i - L + 1 == k:
                if float(curSum) / k >= threshold:
                    res += 1
                curSum -= arr[L]
                L += 1
        
        return res
