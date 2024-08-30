import heapq

# A K-sorted array is an array where each element is at most K positions away from its position in the sorted array. 
def sort_k_sorted_array(arr, k):
    n = len(arr)
    
    # Create a min heap of the first k+1 elements
    min_heap = arr[:k+1]
    heapq.heapify(min_heap)
    
    # Index for where to put the next sorted element
    index = 0
    
    # Process remaining elements
    for i in range(k+1, n):
        # The smallest element in the heap is the next sorted element
        arr[index] = heapq.heappop(min_heap)
        index += 1
        
        # Add the next element to the heap
        heapq.heappush(min_heap, arr[i])
    
    # Pop and place the remaining elements from the heap
    while min_heap:
        arr[index] = heapq.heappop(min_heap)
        index += 1
    
    return arr

# Example usage
arr = [6, 5, 3, 2, 8, 10, 9]
k = 3
sorted_arr = sort_k_sorted_array(arr, k)
print(f"The sorted array is: {sorted_arr}")