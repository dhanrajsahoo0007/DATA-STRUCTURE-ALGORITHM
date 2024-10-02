"""
We are given a list schedule of employees, which represents the working time for each employee.

Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.

Return the list of finite intervals representing common, positive-length free time for all employees, also in sorted order.

(Even though we are representing Intervals in the form [x, y], the objects inside are Intervals, not lists or arrays. For example, schedule[0][0].start = 1, schedule[0][0].end = 2, and schedule[0][0][0] is not defined).  Also, we wouldn't include intervals like [5, 5] in our answer, as they have zero length.



Example 1:

Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
Output: [[3,4]]
Explanation: There are a total of three employees, and all common
free time intervals would be [-inf, 1], [3, 4], [10, inf].
We discard any intervals that contain inf as they aren't finite.

Example 2:

Input: schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
Output: [[5,6],[7,9]]

"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end


class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        """
        The solution’s core revolves around merging overlapping intervals of employees
          and identifying the free time gaps between these merged intervals.
        Using a min-heap,
         -  we arrange the intervals based on when they start,
         -  sorting them according to their start times.
         -  When we pop an element from the min-heap,
            it guarantees that the earliest available interval is returned for processing.
         -  As intervals are popped from the min-heap,
            the algorithm attempts to merge them.
         -  If the currently popped interval’s start time exceeds the
            merged interval’s end time, a gap is identified, indicating a free period.
         -  After identifying each gap,
            the algorithm restarts the merging process to continue 
            identifying additional periods of free time.

        N employees, m intervals
        The time complexity is : O(m log N) 
        The space complexity is O(n)


        """
        import heapq

        heap = []
        employee_count = len(schedule)
        for i in range(employee_count):
            # start time , index and ?
            heap.append( (schedule[i][0].start, i , 0) )
        # Sort the heap and store the elements in the start time ascending order
        heapq.heapify(heap)
        result = []
        # Gets the 0th employee, 0th interval
        previous = schedule[heap[0][1]][heap[0][2]].start

        while heap:
            # O(nlogn)
            _, i,j = heapq.heappop(heap)
            interval = schedule[i][j]

            if interval.start > previous:
                result.append(Interval(previous, interval.start))
    
            previous = max(previous, interval.end)
            if j+1 < len(schedule[i]):
                heapq.heappush(heap, ( schedule[i][j+1].start, i, j+1 ) )
        return result

    # alternate read
    def employeeFreeTime(self, schedule):
        ints = sorted([i for s in schedule for i in s], key=lambda x: x.start)
        res, pre = [], ints[0]
        for i in ints[1:]:
            if i.start <= pre.end and i.end > pre.end:
                pre.end = i.end
            elif i.start > pre.end:
                res.append(Interval(pre.end, i.start))
                pre = i
        return res
"""
With a problem like this it is nice to know when to use python's sorted vs heapq.merge. Since the schedules are already sorted per employee we can take advantage of this fact and use heapq.merge for O(nlogk) time instead of the O(nlogn) for the sorted function. Another benefit is space - sorted pulls all of the data into memory O(n) (even for in place sort) whileheapq.merge returns an iterable O(k).
"""
