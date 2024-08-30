"""
Problem Statement:
    Given a number n and a value k, find the smallest number that can be formed by 
    performing at most k swaps on the digits of n.

Explanation:

Greedy Approach:
    The greedy approach works by iterating through the number from left to right.
    For each position, it finds the smallest digit within the next k positions and swaps it to the current position.
    This ensures that we always have the smallest possible digit in the leftmost position.

Backtracking Approach:
    The backtracking approach tries all possible swaps recursively.
    It starts from the leftmost position and finds the minimum digit from that position to the end.
    If the current digit is not the minimum, it swaps with the rightmost occurrence of the minimum digit.
    This process is repeated for the next position with the remaining swaps.

Recursion Tree for Backtracking (simplified for num = 324 and k = 2):

                   324
                  /   \
               234    324
              /  \    /  \
            234  243 314 324

Note: The actual recursion tree would be much larger for the given example (7654321, k=4).
This simplified tree shows the basic structure of the recursion.


Here's a brief overview of the two approaches:

Greedy Solution:

    Time Complexity: O(n * k)
    Space Complexity: O(n)
    Approach: Iterates through the number from left to right, finding the smallest digit within the next k positions and swapping it to the current position.


Backtracking Solution:

    Time Complexity: O(n^k) in the worst case
    Space Complexity: O(n)
    Approach: Recursively tries all possible swaps, starting from the leftmost position and finding the minimum digit from that position to the end.

"""

def smallest_number_greedy(num, k):
    num = list(str(num))
    n = len(num)
    
    for i in range(n - 1):
        if k == 0:
            break
        
        pos = i
        for j in range(i + 1, min(n, i + k + 1)):
            if num[j] < num[pos]:
                pos = j
        
        for j in range(pos, i, -1):
            num[j], num[j-1] = num[j-1], num[j]
        
        k -= pos - i
    
    return int(''.join(num))

# Time Complexity: O(n * k), where n is the number of digits in num
# Space Complexity: O(n) to store the digits as a list

# Corrected Backtracking Solution
def smallest_number_backtrack(num, k):
    num = list(str(num))
    n = len(num)
    min_num = num[:]
    
    def backtrack(curr, k):
        nonlocal min_num
        if k == 0:
            if curr < min_num:
                min_num = curr[:]
            return
        
        for i in range(n):
            for j in range(i+1, n):
                curr[i], curr[j] = curr[j], curr[i]
                if curr < min_num:
                    backtrack(curr, k-1)
                curr[i], curr[j] = curr[j], curr[i]  # backtrack
    
    backtrack(num, k)
    return int(''.join(min_num))

# Time Complexity: O(n^k) in the worst case, where n is the number of digits in num
# Space Complexity: O(n) for the recursion stack and to store the digits as a list

# Example usage and testing
num = 7654321
k = 4

print(f"Original number: {num}")
print(f"Smallest number after at most {k} swaps (Greedy): {smallest_number_greedy(num, k)}")
print(f"Smallest number after at most {k} swaps (Backtracking): {smallest_number_backtrack(num, k)}")

