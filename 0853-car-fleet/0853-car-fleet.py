class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = [(pos, speed) for pos, speed in zip(position, speed)]
        pos_speed.sort(reverse = True, key = lambda x: x[0])

        stack = []

        for pos, speed in pos_speed:
            time = (target - pos) / speed 
            if stack and stack[-1] >= time:
                time = stack.pop()
            
            stack.append(time)
        
        return len(stack)
