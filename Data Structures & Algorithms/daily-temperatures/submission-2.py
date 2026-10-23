class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        my_stack = []
        for i in range(len(temperatures)):
            while len(my_stack) != 0 and temperatures[my_stack[-1]] < temperatures[i]:
                j = my_stack.pop()
                result[j] = i - j
            my_stack.append(i)
        return result
        