from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadend = set(deadends)
        if "0000" in deadend:
            return -1

        q = deque([("0000", 0)])
        visit = set(["0000"])
        while q:
            cur, turns = q.popleft()
            
            if cur == target:
                return turns
            
            cur_list = list(cur)
            for i in range(4):
                original_char = cur_list[i]
                digit = int(original_char)
                
                for move in (-1, 1):
                    cur_list[i] = str((digit + move) % 10)
                    tmps = ''.join(cur_list)
                    
                    if tmps not in visit and tmps not in deadend:
                        visit.add(tmps)  
                        q.append((tmps, turns + 1))
                
                cur_list[i] = original_char
        
        return -1
