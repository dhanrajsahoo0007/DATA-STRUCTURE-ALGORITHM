"""
Problem Statement: Find the Smallest Divisor Given a Threshold

    Given an array of integers nums and an integer threshold, 
    we will choose a positive integer divisor, divide all the array by it, and sum the division's result.
    Find the smallest divisor such that the 
    
    result mentioned above is less than or equal to threshold.

    Each result of the division is rounded to the nearest integer greater than or equal to that element. 
    (For example: 7/3 = 3 and 10/2 = 5).

Constraints:
    * 1 <= nums.length <= 5 * 10^4
    * 1 <= nums[i] <= 10^6
    * nums.length <= threshold <= 10^6

Time Complexity: O(n * log(max(nums))), where n is the length of the nums array.
    - The binary search takes O(log(max(nums))) iterations.
    - In each iteration, we iterate through the nums array once, which takes O(n) time.

Space Complexity: O(1), as we only use a constant amount of extra space.

"""

from typing import List
import math

def sum_of_divisions(nums: List[int], divisor: int) -> int:

    total = 0
    
    # Iterate through each number in the list
    for num in nums:
        # Calculate the result of division and round up
        # math.ceil() is used because we need to round up even if the result is not a whole number
        total += math.ceil(num / divisor)
    
    return total

def smallest_divisor(nums: List[int], threshold: int) -> int:

    # Initialize the binary search range
    left = 1  # Minimum possible divisor
    right = max(nums)  # Maximum possible divisor (largest number in nums)

    while left < right:
        # Calculate the middle divisor
        mid = left + (right - left) // 2
        
        # Calculate the sum of divisions for the current divisor
        total = sum_of_divisions(nums, mid)
        
        if total <= threshold:
            # If the sum is less than or equal to threshold, try a smaller divisor
            right = mid
        else:
            # If the sum is greater than threshold, we need a larger divisor
            left = mid + 1

    # Return the smallest divisor that satisfies the condition
    return left

# Example usage
if __name__ == "__main__":
    # Example 1
    nums1 = [1, 2, 5, 9]
    threshold1 = 6
    result1 = smallest_divisor(nums1, threshold1)
    print(f"Example 1 - Input: nums = {nums1}, threshold = {threshold1}")
    print(f"Output: {result1}")
    print()

    # Example 2
    nums2 = [44, 22, 33, 11, 1]
    threshold2 = 5
    result2 = smallest_divisor(nums2, threshold2)
    print(f"Example 2 - Input: nums = {nums2}, threshold = {threshold2}")
    print(f"Output: {result2}")