class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position,speed), reverse = True)
        stack = []
        for car in cars:
            timetoreach = (target - car[0]) / car[1]
            if not stack or timetoreach > stack[-1]:
                stack.append(timetoreach)
        return len(stack)

