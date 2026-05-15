class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for index, value in enumerate(temperatures):
            while len(stack) !=0 and temperatures[stack[-1]] < value:
                popped = stack.pop()
                result[popped] = index - popped
            stack.append(index)
        return result

