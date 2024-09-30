from typing import List

class Solution:
    def simulateQueue(self, wait: List[int]) -> List[int]:
        n = len(wait)
        result = [n]  # Initial queue size
        time = 0
        
        # Create a list of (expiration_time, index) pairs
        expirations = [(wait[i], i) for i in range(n)]
        expirations.sort()  # Sort by expiration time
        
        next_to_expire = 0
        queue_size = n
        
        while queue_size > 0:
            time += 1
            queue_size -= 1  # Process the front request
            
            # Remove expired requests
            while next_to_expire < n and expirations[next_to_expire][0] <= time:
                if expirations[next_to_expire][1] > time - 1:
                    queue_size = max(0, queue_size - 1)
                next_to_expire += 1
            
            if queue_size > 0:
                result.append(queue_size)
            else:
                result.append(0)
                break
        
        return result

# Test cases
solution = Solution()
test_cases = [
    [2, 2, 3, 1],
    [3, 1, 2, 1],
    [4, 4, 4]
]
for i, case in enumerate(test_cases, 1):
    result = solution.simulateQueue(case)
    print(f"Test Case {i}:")
    print(f"Input: {case}")
    print(f"Output: {result}")
    print()