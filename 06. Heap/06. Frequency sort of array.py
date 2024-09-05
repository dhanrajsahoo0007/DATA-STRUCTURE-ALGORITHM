from collections import Counter
import heapq



# def frequency_sort_using_map(arr):
#     # Count the frequency of each number
#     freq_count = Counter(arr)
    
#     # Sort the unique elements based on their frequency and value
#     sorted_elements = sorted(freq_count.keys(), key=lambda x: (-freq_count[x], x))
    
#     # Construct the result array
#     result = []
#     for num in sorted_elements:
#         result.extend([num] * freq_count[num])
    
#     return result

# def frequency_sort(arr):
#     # Count the frequency of each number
#     freq_count = Counter(arr)
    
#     # Define a key function for sorting
#     def sort_key(x):
#         return (-freq_count[x], x)
    
#     # Sort the array using the key function
#     return sorted(arr, key=sort_key)

def frequency_sort(arr):
    # Count the frequency of each number
    freq_count = Counter(arr)
    
    # Create a max heap of tuples: (frequency, -value, value)
    # We use -value to sort by higher value when frequencies are equal
    heap = []
    for num, freq in freq_count.items():
        heapq.heappush(heap, (-freq, -num, num))
    
    result = []
    
    # Extract elements from the heap and add to result
    while heap:
        freq, _, num = heapq.heappop(heap)
        result.extend([num] * (-freq))  # Add 'num' to result 'freq' times
    
    return result

# Example usage
arr = [1, 1, 2, 2, 2, 3]
sorted_arr = frequency_sort(arr)
print(f"The frequency sorted array is: {sorted_arr}")

# The use of (-freq, -num, num) is crucial for achieving the correct sorting order. Let's break it down:

# -freq (negative frequency):
    # We use the negated frequency as the first element because Python's heapq module implements a min-heap, but we want a max-heap behavior for frequencies.
    # By negating the frequency, larger frequencies become smaller negative numbers, which will be at the top of the min-heap, effectively giving us max-heap behavior for frequencies.

# -num (negative number):
    # This is used as a tie-breaker when frequencies are equal.
    # We want larger numbers to come first when frequencies are the same, so we negate the number.
    # In a min-heap, smaller values come first, so negating the number ensures larger numbers are treated as "smaller" in the heap.

# num (original number):
    # We keep the original number as the third element in the tuple so we can easily retrieve it when building our result list.



# Here's an example to illustrate:
# Suppose we have numbers 5 and 3, both with a frequency of 2. We'd create these tuples:
# (-2, -5, 5) for number 5
# (-2, -3, 3) for number 3
# In the min-heap, (-2, -5, 5) would come before (-2, -3, 3) because:

# The frequencies (-2) are equal
# -5 is less than -3

# This ensures that when we pop from the heap, we get 5 before 3, which is what we want: among equal frequencies, larger numbers come first.