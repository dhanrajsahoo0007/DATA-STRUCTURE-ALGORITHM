from collections import Counter
import heapq

# Step:-1: We use a Counter to count the frequency of each number in the input array. This gives us a dictionary where keys are the numbers and values are their frequencies.
# Step:-2: We then use a min heap to keep track of the k most frequent elements. We use a min heap (rather than a max heap) because we want to be able to easily remove the least frequent element when the heap is full.
# Step:-3: We iterate through the items in our frequency counter:
            # If the heap has less than k elements, we simply add the current element.
            # If the heap is full (has k elements) and the current frequency is higher than the smallest frequency in the heap, we remove the smallest and add the current one
# Step:-4: The heap stores tuples of (frequency, number). We use the frequency as the first element of the tuple because heapq in Python compares tuples lexicographically.
# Step:-5: Finally, we extract just the numbers from the heap to get our result.


# Time Complexity: O(n log k), where n is the number of elements in the input array. We iterate through all elements once to count frequencies, and then perform at most n heap operations, each taking O(log k) time.
# Space Complexity: O(n) for the counter and O(k) for the heap, so overall O(n).

def top_k_frequent(nums, k):
    # Count the frequency of each number
    count = Counter(nums)
    
    # Use a min heap to keep track of the k most frequent elements
    heap = []
    
    for num, freq in count.items():
        # If the heap has less than k elements, just add the current element
        if len(heap) < k:
            heapq.heappush(heap, (freq, num))
        # If the current frequency is higher than the smallest frequency in the heap,
        # remove the smallest and add the current one
        elif freq > heap[0][0]:
            heapq.heapreplace(heap, (freq, num))
    
    # Extract the numbers from the heap (ignoring their frequencies)
    return [num for freq, num in heap]

# Example usage
nums = [1, 1, 1, 2, 2, 3]
k = 2
result = top_k_frequent(nums, k)
print(f"The {k} most frequent elements are: {result}")