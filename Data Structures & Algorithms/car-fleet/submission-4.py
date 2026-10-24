class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position,speed),reverse=True)
        my_stack = []
        for i in range(len(cars)):
            position[i],speed[i] = cars[i]
            arvv_time = (target-position[i]) / speed[i]
            while len(my_stack) == 0 or my_stack[-1] < arvv_time:
                my_stack.append(arvv_time)
        return len(my_stack)
                
        