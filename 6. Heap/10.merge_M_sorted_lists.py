import heapq


# Step:1 - We create a min-heap (min_heap) to keep track of the smallest elements from each list.
# Step:2 - We initialize the heap by adding the first element from each list. Each entry in the heap is a tuple containing:
#         The value of the element
#         The index of the list it came from
#         The index of the element within its list


# Step:3- We enter a loop that continues until the heap is empty:

#         We pop the smallest element from the heap
#         We add this element to our result list
#         If there are more elements in the list that this element came from, we add the next element from that list to the heap


# Step:4- Once the heap is empty, we've processed all elements, and our result list contains all elements in sorted order.

# The time complexity of this solution is O(N log M), where N is the total number of elements across all lists, and M is the number of lists. 
# This is because each element is pushed and popped from the heap once, and the heap has at most M elements at any time.
# The space complexity is O(M) for the heap, plus O(N) for the output list.


def merge_sorted_lists(lists):
    min_heap = []
    result = []
    
    # Add the first element from each list to the min heap
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(min_heap, (lst[0], i, 0))
    
    # Process elements until the heap is empty
    while min_heap:
        val, list_index, element_index = heapq.heappop(min_heap)
        
        # Add the smallest element to the result
        result.append(val)
        
        # If there are more elements in the list, add the next one to the heap
        if element_index + 1 < len(lists[list_index]):
            next_element = lists[list_index][element_index + 1]
            heapq.heappush(min_heap, (next_element, list_index, element_index + 1))
    
    return result

# Example usage
lists = [
    [1, 4, 5],
    [1, 3, 4],
    [2, 6]
]

merged = merge_sorted_lists(lists)
print("Merged sorted list:", merged)