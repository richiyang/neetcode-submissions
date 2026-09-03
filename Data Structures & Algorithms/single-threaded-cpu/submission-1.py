import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        sortedTasks = [[task[0], task[1], i] for i, task in enumerate(tasks)]
        sortedTasks.sort()
        
        res = []
        t = 0
        i = 0
        h = []
        n = len(tasks)
        
        while i < n or h:
            if not h and t < sortedTasks[i][0]:
                t = sortedTasks[i][0]
            
            while i < n and sortedTasks[i][0] <= t:
                heapq.heappush(h, [sortedTasks[i][1], sortedTasks[i][2]])
                i += 1

            procTime, index = heapq.heappop(h)
            t += procTime
            res.append(index)
        
        return res

