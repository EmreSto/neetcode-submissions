class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        my_stack = []
        cars = sorted(zip(position,speed),reverse=True)
        for i in range(len(cars)):
            position[i],speed[i] = cars[i]
            arv_time = (target - position[i]) / speed[i]
            while len(my_stack) == 0 or my_stack[-1] < arv_time:
                my_stack.append(arv_time)
        return len(my_stack)




        