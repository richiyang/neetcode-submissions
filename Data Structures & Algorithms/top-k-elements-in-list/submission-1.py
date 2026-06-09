class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int)
        buckets = [[] for _ in range(len(nums) + 1)]
        res = []

        for num in nums:
            freqs[num] += 1
        
        for num, freq in freqs.items():
            buckets[freq].append(num)
        
        for b in range(len(buckets) - 1, -1, -1):
            for i in buckets[b]:
                res.append(i)
                if len(res) == k:
                    return res