"""
Problem Statement:
    Given a string and an integer K, find the length of the longest substring that contains exactly K unique characters.

Explanation:
We use a variable size sliding window technique with a dictionary to keep track of character frequencies:
    1. Use two pointers, i and j, to define the window.
    2. Use a dictionary to store the frequency of characters in the current window.
    3. Maintain a count of unique characters in the current window.
    4. Expand the window by moving j to the right, updating the character count and unique character count.
    5. If unique character count exceeds K, shrink the window from the left until we again have K unique characters.
    6. Update the maximum length whenever we have exactly K unique characters.

Time Complexity: O(n), where n is the length of the string.
Space Complexity: O(K), where K is the number of unique characters we're looking for.
"""

def longest_k_unique_substring(s, k):
    char_freq = {}
    i = j = 0
    max_length = -1
    unique_count = 0
    n = len(s)

    while j < n:
        # If character is not in map or its frequency is 0, increment unique_count
        if s[j] not in char_freq or char_freq[s[j]] == 0:
            unique_count += 1
        
        # Update character frequency
        char_freq[s[j]] = char_freq.get(s[j], 0) + 1

        if unique_count < k:
            j += 1
        elif unique_count == k:
            
            max_length = max(max_length, j - i + 1)
            j += 1
        else:  # unique_count > k
            # Shrink the window until we have exactly K unique characters
            while unique_count > k:
                char_freq[s[i]] -= 1
                if char_freq[s[i]] == 0:
                    unique_count -= 1
                i += 1
            # After shrinking, if we have exactly K unique characters, update max_length
            if unique_count == k:
                max_length = max(max_length, j - i + 1)
            j += 1

    return max_length

# Test cases
def run_test_case(s, k):
    result = longest_k_unique_substring(s, k)
    print(f"String: {s}")
    print(f"K: {k}")
    print(f"Output: {result}")
    print()

# Test cases
run_test_case("aabacbebebe", 3)
run_test_case("abcdefg", 3)
run_test_case("aaabbb", 3)
run_test_case("aabbcc", 3)
run_test_case("", 2)
run_test_case("aaabbbccc", 1)
run_test_case("abcbdbdbbdcdabd", 2)
