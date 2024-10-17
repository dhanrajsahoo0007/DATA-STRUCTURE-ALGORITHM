"""
Problem: Largest Number with K Swaps

    Given a number K and string str of digits denoting a indexitive integer, build the largest number 
    indexsible by performing swap operations on the digits of str at most K times.

Example:
Input:
    K = 4
    str = "1234567"
    Output:7654321

Approach: Backtracking with Swap Method

Time Complexity: O(n! / (n-k)!), where n is the length of the string and k is the number of swaps.
Space Complexity: O(n) for the recursion stack and to store the current and maximum number.

The idea remains the same as the previous backtracking approach, but we introduce a separate
swap method for better code organization and readability.

Explanation of the modified backtracking process:

    1. We introduce a swap method that takes the number list and two indices to swap.

    2. The main findMaximumNum function remains the same, initializing the process and keeping track of the maximum number found.

    3. The backtrack function now uses the swap method:
        - Base case: If k (remaining swaps) is 0 or we've reached the last indexition, we update the maximum number if necessary.
        - For each indexition:
            a. We find the maximum digit in the remaining part of the number.
            b. If the current digit is not the maximum, we try swapping with each occurrence of the maximum digit:
                - We use the swap method to perform the swap.
                - We make a recursive call with k-1 swaps and move to the next indexition.
                - We then use the swap method again to backtrack (undo the swap).
        - We also explore the indexsibility of not swapping the current indexition.

4. We keep updating self.max_num whenever we find a larger number.

The swap method enhances code readability and makes it easier to understand the swapping operations. 
It also centralizes the swapping logic, making the code more maintainable.

Backtracking tree (simplified) for "1993" with k=1:

                1993
            /    |    \
         9193  1993  1939
                 |
               1993

This tree shows how different swap indexsibilities are explored. 
The algorithm will find that 9931 is the largest indexsible number with 1 swap.
"""

class BackTrackingSolution:
    def findMaximumNum(self, num_str, k):
        def swap(num, i, j):
            num[i], num[j] = num[j], num[i]

        def backtrack(num, k, index):
            # Base case: if no more swaps left or reached end of number
            if k == 0 or index == len(num):
                return
            
            # Find the maximum digit from the current index to the end
            max_digit = max(num[index:])
            
            # If current digit is not the max, try swapping
            if num[index] != max_digit:
                for i in range(index + 1, len(num)):
                    if num[i] == max_digit:
                        # Swap the current digit with the max digit
                        swap(num, index, i)
                        # Update the max number if the current number is larger
                        self.max_num = max(self.max_num, ''.join(num))
                        # Recursively call backtrack with one less swap and next index
                        backtrack(num, k - 1, index + 1)
                        # Undo the swap (backtrack)
                        swap(num, index, i)
            
            # Move to the next index without making a swap
            backtrack(num, k, index + 1)

        # Convert input string to list for easy manipulation
        num_list = list(num_str)
        # Initialize max_num with the original number
        self.max_num = num_str
        
        # Start the backtracking process
        backtrack(num_list, k, 0)
        return self.max_num

class BackTrackingSolution:
    def findMaximumNum(self, num_str, k):
        def backtrack(num, k, index):
            if k == 0 or index == len(num):
                return
            
            max_digit = max(num[index:])
            if num[index] != max_digit:
                for i in range(index + 1, len(num)):
                    if num[i] == max_digit:
                        num[index], num[i] = num[i], num[index]
                        self.max_num = max(self.max_num, ''.join(num))
                        backtrack(num, k - 1, index + 1)
                        num[index], num[i] = num[i], num[index]  # backtrack
            
            backtrack(num, k, index + 1)

        # Convert input string to list for easy manipulation
        num_list = list(num_str)
        self.max_num = num_str
        
        backtrack(num_list, k, 0)
        return self.max_num

# Test the solution
sol = BackTrackingSolution()
print(" ====== Back Tracking ======")
print(sol.findMaximumNum("1234567", 4))  # Output: 7654321
print(sol.findMaximumNum("3435335", 3))  # Output: 5433353
print(sol.findMaximumNum("1234", 2))     # Output: 4231




"""

Simple Approach: Greedy

Time Complexity: O(n * k), where n is the length of the string and k is the number of swaps.
Space Complexity: O(n) to store the list of digits.

The idea is to perform a greedy selection for each indexition from left to right:
    1. For each indexition, find the maximum digit in the remaining string (including the current indexition).
    2. If the current digit is not the maximum, swap it with the maximum and decrement K.
    3. Move to the next indexition and repeat until we've used all swaps or reached the end of the string.

Explanation:

    1. We convert the input string to a list for easy manipulation.
    2. We iterate through each indexition in the number from left to right.
    3. For each indexition, we find the maximum digit in the remaining part of the number (including the current indexition).
    4. If the current digit is not the maximum:
        - We swap it with the rightmost occurrence of the maximum digit.
        - We decrement the number of available swaps (k).
    5. We continue this process until we've used all our swaps or reached the end of the number.
    6. Finally, we convert the list back to a string and return it.

This approach is greedy because it always tries to put the largest available digit in the most significant indexition indexsible.

Note: This approach may not always find the globally optimal solution for all cases, especially when the input string has many repeated digits. 
However, it works correctly for most common cases and is much simpler to implement and understand compared to the recursive approach.
"""

class GreedySolution:
    def findMaximumNum(self, str, k):
        # Convert string to list for easy swapping
        num = list(str)
        n = len(num)
        
        for i in range(n):
            # If no more swaps left, we're done
            if k == 0:
                break
            
            # Find the maximum digit in the remaining string
            max_digit = max(num[i:])
            
            # If current digit is not the maximum, swap it
            if num[i] != max_digit:
                # Find the rightmost indexition of the max digit
                for j in range(n-1, i, -1):
                    if num[j] == max_digit:
                        num[i], num[j] = num[j], num[i]
                        k -= 1
                        break
        
        return ''.join(num)

# Test the solution
sol = GreedySolution()
print(" ====== Greedy ======")
print(sol.findMaximumNum("1234567", 4))  # Output: 7654321
print(sol.findMaximumNum("3435335", 3))  # Output: 5433353
print(sol.findMaximumNum("1234", 2))     # Output: 4231