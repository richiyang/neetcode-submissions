class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        speedMap = {}
        for i in range(len(position)):
            speedMap[position[i]] = speed[i]
        
        position.sort(reverse = True)

        stack = []
        for i in range(len(position)):
            time = (target - position[i]) / speedMap[position[i]]

            if not stack:
                stack.append(time)
                continue

            if time > stack[-1]:
                stack.append(time)
                continue
        
        return len(stack)

