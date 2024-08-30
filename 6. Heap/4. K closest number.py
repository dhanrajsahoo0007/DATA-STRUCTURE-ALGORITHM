import heapq


# Uses Python's heapq module to maintain a max heap of size k.
# Step - 1: Iterates through the list once, keeping track of the k closest numbers seen so far.
# Step - 2: For each number, if we haven't found k numbers yet, we add it to the heap.
# Step - 3: If we've already found k numbers, we compare the current number to the furthest number in our heap. If it's closer, we remove the furthest and add the current number.

def find_k_closest(numbers, target, k):
    # Use a max heap to keep track of the k closest numbers
    heap = []
    
    for num in numbers:
        diff = abs(num - target)
        
        # If we haven't found k numbers yet, add to the heap
        if len(heap) < k:
            heapq.heappush(heap, (-diff, num))
        else:
            # If this number is closer than the furthest in our heap,
            # remove the furthest and add this one
            if diff < -heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap, (-diff, num))
    
    # Extract the numbers from the heap
    return [num for _, num in heap]

# Example usage
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 5
k = 3

result = find_k_closest(numbers, target, k)
print(f"The {k} closest numbers to {target} are: {result}")