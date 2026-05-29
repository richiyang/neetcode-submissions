import heapq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = collections.defaultdict(list)
        for i in range(len(edges)):
            adj[edges[i][0]].append([edges[i][1], succProb[i]])
            adj[edges[i][1]].append([edges[i][0], succProb[i]])
        
        maxProb = [0] * n
        maxProb[start_node] = 1
        maxHeap = [[-1, start_node]]
        while maxHeap:
            p1, n1 = heapq.heappop(maxHeap)
            if n1 == end_node:
                return -p1
            if -p1 < maxProb[n1]:
                continue

            for n2, p2 in adj[n1]:
                p = p1 * p2
                if -p > maxProb[n2]:
                    maxProb[n2] = -p
                    heapq.heappush(maxHeap, [p1 * p2, n2])
        
        return 0
