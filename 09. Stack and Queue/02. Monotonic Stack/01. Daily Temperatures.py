from typing import List

class Solution:
    def dailyTemperatures_reverse(self, temperatures: List[int]) -> List[int]:
        """
        Calculates the number of days to wait for a warmer temperature using reverse iteration.
        
        Time Complexity: O(n), where n is the length of the temperatures list.
        Space Complexity: O(n)
        """
        n = len(temperatures)
        result = [0] * n  # Initialize result array with zeros
        stack = []  # Stack to store indices
        
        # Traverse the array from right to left
        for i in range(n - 1, -1, -1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            
            if stack:
                # If stack is not empty, top of stack is the next warmer day
                result[i] = stack[-1] - i
            # If stack is empty, result[i] remains 0 (no warmer day found)
            
            # Push current index to stack for future comparisons
            stack.append(i)
        
        return result

    def dailyTemperatures_forward(self, temperatures: List[int]) -> List[int]:
        """
        Calculates the number of days to wait for a warmer temperature using forward iteration.
        
        Time Complexity: O(n), where n is the length of the temperatures list.
        Space Complexity: O(n)
        """
        n = len(temperatures)
        answer = [0] * n 
        stack = []  
        
        for i in range(n):
            # While stack is not empty and current temperature is higher than temperature at top of stack
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                answer[prev_index] = i - prev_index
            
            stack.append(i)
        
        return answer

# Test cases
solution = Solution()

test_cases = [
    [73,74,75,71,69,72,76,73],
    [30,40,50,60],
    [30,60,90]
]

for i, temperatures in enumerate(test_cases, 1):
    print(f"Example {i}:")
    print("Input:", temperatures)
    print("Output (Reverse):", solution.dailyTemperatures_reverse(temperatures))
    print("Output (Forward):", solution.dailyTemperatures_forward(temperatures))
    print()