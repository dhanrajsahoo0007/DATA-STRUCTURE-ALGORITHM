
# Question: Find the median of a stream 

# Step-1: We maintain two heaps:
#         small: A max heap containing the smaller half of the numbers.
#         large: A min heap containing the larger half of the numbers.

# Step-2: In the addNum method:

#             We first push the new number to small (as a negative number to simulate a max heap).
#             We then move the largest number from small to large.
#             If large becomes larger than small, we move one number back to small.
#             This ensures that small always has either the same number of elements as large, or one more.

# Step-3: In the findMedian method:

#             If small has more elements, the median is the top of small.
#             If they have the same number of elements, the median is the average of the tops of both heaps.

# Time Complexity:
#     addNum: O(log n) for heap operations.
#     findMedian: O(1) as we're just accessing the tops of the heaps.

# Space Complexity: O(n) to store all the numbers.

import heapq
class MedianFinder:
    def __init__(self):
        self.small = []  # max heap for the smaller half
        self.large = []  # min heap for the larger half

    def addNum(self, num: int) -> None:
        # Push to the max heap and then move the largest to the min heap
        heapq.heappush(self.small, -num)
        heapq.heappush(self.large, -heapq.heappop(self.small))
        
        # Balance the heaps
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        else:
            return (self.large[0] - self.small[0]) / 2

# Example usage
mf = MedianFinder()
mf.addNum(1)
mf.addNum(2)
mf.addNum(4)
mf.addNum(6)
mf.addNum(9)
mf.addNum(4)
print(mf.findMedian())  # Output: 1.5
mf.addNum(30)
mf.addNum(31)
mf.addNum(32)
mf.addNum(37)
mf.addNum(48)
mf.addNum(58)
print(mf.findMedian())  # Output: 2