import heapq



# We use a max heap to keep track of the K closest points. The heap stores tuples of (-distance, point).
# We iterate through all points:
#     Calculate the squared distance from the origin (x^2 + y^2). We use squared distance to avoid the computationally expensive square root operation.
#     If we have less than K points in our heap, we add the current point.
#     If we have K points and the current point is closer than the furthest point in our heap, we remove the furthest point and add the current one.


# The negative of the distance is used in the heap so that the point with the largest distance is at the top of the max heap.
# Finally, we extract and return the points from the heap.

# Time complexity of O(n * log(k)), where n is the number of points
def k_closest_points(points, k):
    # Use a max heap to keep track of the k closest points
    heap = []
    
    for x, y in points:
        # Calculate distance squared (no need for square root)
        dist = x*x + y*y
        
        if len(heap) < k:
            # If we have less than k points, add to the heap
            heapq.heappush(heap, (-dist, [x, y]))
        elif -dist > heap[0][0]:
            # If this point is closer than the furthest in our heap,
            # remove the furthest and add this one
            heapq.heappop(heap)
            heapq.heappush(heap, (-dist, [x, y]))
    
    # Extract the points from the heap
    return [point for _, point in heap]

# Example usage
points = [[1,3],[-2,2],[5,8],[0,1]]
k = 2

result = k_closest_points(points, k)
print(f"The {k} closest points to the origin are: {result}")