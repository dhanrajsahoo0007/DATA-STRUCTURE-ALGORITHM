"""
You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.

The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].


Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

"""
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        """
        We’ll use two indexes, i and j, to iterate through the intervals in both lists,
        To check whether there’s any intersecting point among the given intervals:
          - Take the starting times of the first pair of intervals from both lists and check which occurs later, storing it in a variable,  start.
          - Also, compare the ending times of the same pair of intervals from both lists and store the minimum end time in another variable,  end.
        Next, we will check if firstList[i] and secondList[j] overlap by comparing the start and end times.
        If the times overlap, then the intersecting time interval will be added to the resultant list, that is, intersections.

        After the comparison, we need to move forward in one of the two input lists.
         - The decision is taken based on which of the two intervals being compared ends earlier.
         - If the interval that ends first is in firstList, we move forward in that list, else, we move forward in secondList.
         Time complexity O(n+m)
         Space Complexity (1)
        """
        i = 0
        j = 0
        n =  len(firstList)
        m = len(secondList)
        intersections = []
        while i < n and j < m:
            # Which occurs later
            start = max( firstList[i][0], secondList[j][0])
            # Which ends earlier
            end = min(firstList[i][1], secondList[j][1])
            # for non overlapping intervals, this will not hold true
            # one will start at x to y and the other will be y+1, z+1
            if start <= end:
                intersections.append([start, end])
            # Which ever ends first, move that window
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
        return intersections

