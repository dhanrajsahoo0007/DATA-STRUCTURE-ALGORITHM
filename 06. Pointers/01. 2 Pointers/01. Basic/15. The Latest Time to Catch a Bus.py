from typing import List

class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        # Sort buses and passengers in ascending order
        buses.sort()
        passengers.sort()
        
        # Initialize variables
        n, m = len(buses), len(passengers)
        j = 0  # Pointer for passengers
        count = 0  # Count of passengers on current bus
        
        # Process each bus
        for i in range(n):
            count = 0
            # Load passengers onto the current bus
            while j < m and passengers[j] <= buses[i] and count < capacity:
                j += 1
                count += 1
        
        # Find the latest time to arrive
        latest_time = buses[-1] if count < capacity else passengers[j-1]
        
        # Check if we can arrive at any time before the last passenger
        j -= 1
        while j >= 0 and latest_time == passengers[j]:
            latest_time -= 1
            j -= 1
        
        return latest_time

# Test the solution
if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1
    buses1 = [10, 20]
    passengers1 = [2, 17, 18, 19]
    capacity1 = 2
    print(f"Test case 1 result: {sol.latestTimeCatchTheBus(buses1, passengers1, capacity1)}")
    
    # Test case 2
    buses2 = [20, 30, 10]
    passengers2 = [19, 13, 26, 4, 25, 11, 21]
    capacity2 = 2
    print(f"Test case 2 result: {sol.latestTimeCatchTheBus(buses2, passengers2, capacity2)}")