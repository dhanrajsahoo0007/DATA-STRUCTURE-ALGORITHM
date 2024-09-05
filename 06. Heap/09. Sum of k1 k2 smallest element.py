# Problem Statement:
# Given an array of integers and two numbers k1 and k2, we need to find the sum of all elements between the k1'th smallest and k2'th smallest elements of the array (k1 < k2).




# Example:
# For the array [20, 8, 22, 4, 12, 10, 14] with k1 = 3 and k2 = 6:
#     The 3rd smallest element (k1) is 10
#     The 6th smallest element (k2) is 20
#     The elements between 10 and 20 are 12 and 14
#     So the sum is 12 + 14 = 26

import heapq

# Explanation:
#     We first check if the input is valid (k1 should be less than k2, and k2 should not exceed the array length).
#     We use a helper function find_kth_smallest to find the k'th smallest element. This function uses a max heap of size k to efficiently find the k'th smallest element in O(n log k) time.
#     We find both the k1'th and k2'th smallest elements.
#     We then sum all elements in the array that are strictly between these two values.

def sum_between_k1_and_k2(arr, k1, k2):
    if k1 >= k2 or k2 > len(arr):
        return 0  # Invalid input

    # Find k2'th smallest element
    k2_smallest = find_kth_smallest(arr, k2)
    
    # Find k1'th smallest element
    k1_smallest = find_kth_smallest(arr, k1)
    
    # Sum elements between k1_smallest and k2_smallest
    result = sum(x for x in arr if k1_smallest < x < k2_smallest)
    
    return result

def find_kth_smallest(arr, k):
    # Use a max heap of size k
    heap = []
    for num in arr:
        if len(heap) < k:
            heapq.heappush(heap, -num)  # Push negative for max heap behavior
        elif -num > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, -num)
    return -heap[0]  # Return negative to get actual value

# Example usage
arr = [20, 8, 22, 4, 12, 10, 14]
k1 = 3
k2 = 6

result = sum_between_k1_and_k2(arr, k1, k2)
print(f"The sum of elements between {k1}'th and {k2}'th smallest elements is: {result}")