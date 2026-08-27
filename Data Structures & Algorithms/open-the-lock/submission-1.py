from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        q = deque([("0000", 0)])
        deadend = set(deadends)
        visit = set(["0000"])
        while q:
            cur, turns = q.popleft()
            if cur in deadends:
                continue
            if cur == target:
                return turns
            cur = list(cur)
            for i in range(len(cur)):
                tmp = cur[i]
                cur[i] = str((int(tmp) - 1) % 10)
                tmps = "".join(cur)
                if tmps not in visit and tmps not in deadend:
                    q.append((tmps, turns + 1))
                    visit.add(tmps)
                
                cur[i] = str((int(tmp) + 1) % 10)
                tmps = "".join(cur)
                if tmps not in visit and tmps not in deadend:
                    q.append((tmps, turns + 1))
                    visit.add(tmps)
                cur[i] = tmp
        
        return -1
                

        
