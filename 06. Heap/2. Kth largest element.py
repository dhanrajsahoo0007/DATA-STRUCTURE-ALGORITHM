import heapq

def kth_largest_heap(arr, k):
    if k < 1 or k > len(arr):
        return None
    
    # Create a max heap of the first k elements
    min_heap = arr[:k]
    heapq.heapify(min_heap)
    
    # If we take the k in range then we don't have to check the len(max_heap)
    for i in range(k, len(arr)):
        if arr[i] > min_heap[0]:
            heapq.heapreplace(min_heap, arr[i])
    
    # The root of the heap is the kth smallest element
    return min_heap[0]


# Example usage
arr = [7, 10, 4, 3, 20, 15]
k = 3
result = kth_largest_heap(arr, k)
print(f"The {k}th largest element is: {result}")