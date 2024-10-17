"""
91. Decode Ways
Solved
Medium
Topics
Companies
You have intercepted a secret message encoded as a string of numbers. The message is decoded via the following mapping:

"1" -> 'A'

"2" -> 'B'

...

"25" -> 'Y'

"26" -> 'Z'

However, while decoding the message, you realize that there are many different ways you can decode the message because some codes are contained in other codes ("2" and "5" vs "25").

For example, "11106" can be decoded into:

"AAJF" with the grouping (1, 1, 10, 6)
"KJF" with the grouping (11, 10, 6)
The grouping (1, 11, 06) is invalid because "06" is not a valid code (only "6" is valid).
Note: there may be strings that are impossible to decode.

Given a string s containing only digits, return the number of ways to decode it. If the entire string cannot be decoded in any valid way, return 0.

The test cases are generated so that the answer fits in a 32-bit integer.

 

Example 1:

Input: s = "12"

Output: 2

Explanation:

"12" could be decoded as "AB" (1 2) or "L" (12).

Example 2:

Input: s = "226"

Output: 3

Explanation:

"226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Example 3:

Input: s = "06"

Output: 0

Explanation:

"06" cannot be mapped to "F" because of the leading zero ("6" is different from "06"). In this case, the string is not a valid encoding, so return 0.

 

Constraints:

1 <= s.length <= 100
s contains only digits and may contain leading zero(s).
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        num_ways = 0
        n = len(s)
        memo = {}

        def dfs(starting_index: int) -> int:
            if starting_index == n:
                return 1
            if starting_index in memo:
                return memo[starting_index]
            ans = 0
            if s[starting_index] == "0":
                return ans
            ans += dfs(starting_index+1)
            # check if the char + next char is within 10 and 27
            if starting_index < n - 1 and (
                10 <= (int(s[starting_index: starting_index+2])) < 27
            ):
               ans += dfs(starting_index+2)
            memo[starting_index] = ans
            return memo[starting_index]
                   
        num_ways = dfs(0)
        return num_ways if num_ways > 0 else 0
