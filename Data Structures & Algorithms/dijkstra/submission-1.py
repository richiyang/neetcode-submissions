import heapq

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = defaultdict(list)

        for s, d, w in edges:
            adj[s].append((d, w))
        
        shortest = {}
        minHeap = [(0, src)]

        while minHeap:
            w1, v1 = heapq.heappop(minHeap)
            if v1 in shortest:
                continue
            shortest[v1] = w1

            for v2, w2 in adj[v1]:
                if v2 not in shortest:
                    heapq.heappush(minHeap, (w1 + w2, v2))

        for i in range(n):
            if i not in shortest:
                shortest[i] = -1
        
        return shortest
            