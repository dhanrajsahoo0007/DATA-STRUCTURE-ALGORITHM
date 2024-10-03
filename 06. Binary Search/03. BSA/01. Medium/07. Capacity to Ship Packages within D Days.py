
"""
Capacity To Ship Packages Within D Days

Problem Statement:
    A conveyor belt has packages that must be shipped from one port to another within 'days' days.
    The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights).
    We may not load more weight than the maximum weight capacity of the ship.
    Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within 'days' days.

Examples:
    Example 1:
    Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
    Output: 15
    Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
    1st day: 1, 2, 3, 4, 5
    2nd day: 6, 7
    3rd day: 8
    4th day: 9
    5th day: 10

    Example 2:
    Input: weights = [3,2,2,4,1,4], days = 3
    Output: 6
    Explanation: A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
    1st day: 3, 2
    2nd day: 2, 4
    3rd day: 1, 4

    Example 3:
    Input: weights = [1,2,3,1,1], days = 4
    Output: 3
    Explanation:
    1st day: 1
    2nd day: 2
    3rd day: 3
    4th day: 1, 1

Constraints:
    * 1 <= days <= weights.length <= 5 * 10^4
    * 1 <= weights[i] <= 500

Solution Explanation:
    The solution uses a binary search approach to find the minimum ship capacity:

    1. We define a helper function 'possible' that checks if it's possible to ship all packages within the given days for a specific ship capacity.
    2. In the main function 'shipWithinDays', we perform a binary search on the possible capacity range:
       - The minimum possible capacity is the maximum weight in the weights list.
       - The maximum possible capacity is the sum of all weights.
    3. We keep narrowing down our search range until we find the minimum capacity that allows shipping all packages within the given days.

Time Complexity: O(n * log(sum(weights))), where n is the number of packages.
    - The binary search takes O(log(sum(weights))) iterations.
    - In each iteration, we call the 'possible' function which takes O(n) time.

Space Complexity: O(1), as we only use a constant amount of extra space.
"""

from typing import List

class Solution:
    def possible(self, weight: int, weights: List[int], days: int) -> bool:
        curr_day_count = 1
        curr_sum_weight = 0
        for w in weights:
            curr_sum_weight += w
            
            if curr_sum_weight > weight:
                curr_day_count += 1
                curr_sum_weight = w
            
        return curr_day_count <= days
        """
            Why curr_day_count <= days ?
            Because it is mentioned in the question that all the packages
            need to be shipped "WITHIN" 'days' days
            So, even if we are able to transfer all the weights within
            days < (given days in input) we are good to go.
        """
    
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        n = len(weights)
        
        min_weight = sum(weights)
        max_wt = max(weights)
        
        if n < days:
            return -1  # not possible case
        
        if days == 1:
            return min_weight
        
        high = min_weight
        low = max_wt  # weight cannot be less than maximum weight
        """
        Why ?
        Because in worst case we will have to carry one weight per day.
        So, in that case our ship's capacity must not be less than the maximum weight.
        """
        while low < high:
            mid = low + (high - low) // 2
            
            if self.possible(mid, weights, days):
                high = mid
            else:
                low = mid + 1
        
        return high



# Example usage
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    weights1 = [1,2,3,4,5,6,7,8,9,10]
    days1 = 5
    result1 = solution.shipWithinDays(weights1, days1)
    print(f"Example 1 - Input: weights = {weights1}, days = {days1}")
    print(f"Output: {result1}")
    print()

    # Example 2
    weights2 = [3,2,2,4,1,4]
    days2 = 3
    result2 = solution.shipWithinDays(weights2, days2)
    print(f"Example 2 - Input: weights = {weights2}, days = {days2}")
    print(f"Output: {result2}")
    print()

    # Example 3
    weights3 = [1,2,3,1,1]
    days3 = 4
    result3 = solution.shipWithinDays(weights3, days3)
    print(f"Example 3 - Input: weights = {weights3}, days = {days3}")
    print(f"Output: {result3}")