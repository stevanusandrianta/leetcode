class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i, el in enumerate(temperatures):
            while len(stack) > 0 and el > stack[-1][0]:
                popped_el = stack.pop()
                result[popped_el[1]] = i-popped_el[1]    
            stack.append((el,i))

        return result