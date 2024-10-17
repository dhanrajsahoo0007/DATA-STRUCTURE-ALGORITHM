"""
Problem Statement:
Given an integer N, find all N-digit numbers with digits in strictly increasing order.

Time Complexity: O(9! / (9-N)!)
- In the worst case (N=9), we have 9 choices for the first digit, 8 for the second, 7 for the third, and so on.
- This gives us 9 * 8 * 7 * ... * (10-N) operations, which is 9! / (9-N)!

Space Complexity: O(N)
- The recursion stack can go up to depth N
- We also store the result list, but its size is not dependent on the input size in a way that would change the complexity class

Explanation:
The solution uses a backtracking approach to generate all valid numbers:
1. We start with an empty number and gradually build it up.
2. For each position, we try all possible digits that are greater than the last digit used.
3. When we've placed N digits, we add the number to our result list.
4. We then backtrack to try other possibilities.

Examples:
N = 2: [12, 13, 14, 15, 16, 17, 18, 19, 23, 24, 25, 26, 27, 28, 29, 34, 35, 36, 37, 38, 39, 45, 46, 47, 48, 49, 56, 57, 58, 59, 67, 68, 69, 78, 79, 89]
"""

class BackTrackingSolution:
    def findIncreasingNumbers(self, N):
        def backtrack(num, start, remaining):
            # Base case: if we've added N digits, add the number to our result
            if remaining == 0:
                self.result.append(int(''.join(map(str, num))))
                return
            
            # Try adding each digit from start to 9
            for digit in range(start, 10):
                num.append(digit)
                # Recursively build the number with one less remaining digit
                # and start from the next digit
                backtrack(num, digit + 1, remaining - 1)
                num.pop()  # backtrack by removing the last digit

        self.result = []  # Initialize the result list
        backtrack([], 1, N)  # Start backtracking from 1 as we want strictly increasing
        return self.result

# Test the solution
sol = BackTrackingSolution()
print(" ====== N Digit Numbers with Increasing Digits ======")
print("2-digit numbers:", sol.findIncreasingNumbers(2))
print("3-digit numbers:", sol.findIncreasingNumbers(3))
