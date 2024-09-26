





# Input array: [100, 2, 70, 2, 8, 70, 100]

# Sorted unique elements: [2, 8, 70, 100]
# Rank dictionary: {2: 1, 8: 2, 70: 3, 100: 4}
# Replacing elements with ranks:
    # 100 -> 4
    # 2 -> 1
    # 70 -> 3
    # 2 -> 1
    # 8 -> 2
    # 70 -> 3
    # 100 -> 4
# Output: [4, 1, 3, 1, 2, 3, 4]


def replace_with_rank(arr):
    # Create a sorted copy of the array
    sorted_arr = sorted(set(arr))
    
    # Create a dictionary to store the rank of each element
    rank_dict = {val: rank + 1 for rank, val in enumerate(sorted_arr)}
    
    # Replace each element with its rank
    result = [rank_dict[val] for val in arr]
    
    return result

# Example usage
arr = [100, 2, 70, 2, 8, 70, 100]
result = replace_with_rank(arr)
print(result)  # Output: [4, 1, 3, 1, 2, 3, 4]

# Time Complexity:

#     Sorting the unique elements: O(n log n), where n is the number of unique elements in the array.
#     Creating the rank dictionary: O(n)
#     Replacing elements with ranks: O(m), where m is the length of the original array.
#     Overall time complexity: O(n log n + m)

# Space Complexity:

#     O(n) for the sorted array and the rank dictionary, where n is the number of unique elements.
#     O(m) for the result array, where m is the length of the original array.
#     Overall space complexity: O(n + m)