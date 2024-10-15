"""
777. Swap Adjacent in LR String
Medium

In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL",
 a move consists of either replacing one occurrence of "XL" with "LX",
 or replacing one occurrence of "RX" with "XR". Given the starting string 
 start and the ending string end, return True if and only if there exists
  a sequence of moves to transform start to end.

 
Example 1:

Input: start = "RXXLRXRXL", end = "XRLXXRRLX"
Output: true
Explanation: We can transform start to end following these steps:
RXXLRXRXL ->
XRXLRXRXL ->
XRLXRXRXL ->
XRLXXRRXL ->
XRLXXRRLX
Example 2:

Input: start = "X", end = "L"
Output: false
 

Constraints:

1 <= start.length <= 104
start.length == end.length
Both start and end will only consist of characters in 'L', 'R', and 'X'.
"""
class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        """
        First replace the x in the string and check if the orders of lr are the same in start and end
        There are three kinds of characters, ‘L’, ‘R’, ‘X’.
            Replacing XL with LX = move L to the right by one
            Replacing RX with XR = move R to the left by one
            If we remove all the X in both strings, the resulting strings should be the same.
        Since a move always involves X, an L or R cannot move through another L or R.
        Since an L can only move to the right,
         for each occurrence of L in the start string,
          its position should be to the same or to the left of its corresponding L in the end string.
        """
        if start.replace('X', '') != end.replace('X', ''):
            return False
        
        # The left start positions from the start should be to the left of the left starting positions on the end 
        l_start_positions = [pos for pos in range(len(start)) if start[pos] == "L"]
        l_end_positions = [pos for pos in range(len(end)) if end[pos] == "L"]

        r_start_positions = [pos for pos in range(len(start)) if start[pos] == "R"]
        r_end_positions = [pos for pos in range(len(start)) if end[pos] == "R"]

        for l_start_pos, l_end_pos in zip(l_start_positions, l_end_positions):
            # Since the L from start can go right, it has to be to the left of the L on the end string
            if l_start_pos < l_end_pos:
                return False
        for r_start_pos, r_end_pos in zip(r_start_positions, r_end_positions):
            # Since the R from start can go left, it has to be to the right of the L on the end string
            if r_start_pos > r_end_pos:
                return False
        return True
        
