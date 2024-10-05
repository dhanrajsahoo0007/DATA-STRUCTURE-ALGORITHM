"""
Given a string, input_str, return the length of the longest substring without repeating characters.


Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Iterate over the array, when a duplicate is found ,try shrinking the window to not have a duplicate
        Time complexity: O(N)
        Space Complexity O(1)
        """
        longest_window_len = 0
        char_set = set()
        window_start = 0
        window_end = 0
        while window_end < len(s):
            current_char = s[window_end]
            while current_char in char_set and window_start < window_end:
                char_to_remove = s[window_start]
                window_start += 1
                char_set.remove(char_to_remove)
            char_set.add(current_char)
            current_len = window_end - window_start + 1
            longest_window_len = max(current_len, longest_window_len)
            window_end += 1
        return longest_window_len

# Test function
def run_test_case(s):
    result = Solution().lengthOfLongestSubstring(s)
    print(f"String: {s}")
    print(f"Output: {result}")
    print()

# Test cases
run_test_case("abcabcbb")
run_test_case("bbbbb")
run_test_case("pwwkew")
run_test_case("")
run_test_case("dvdf")
run_test_case("tmmzuxt")
run_test_case("abcdefghijklmnopqrstuvwxyz")