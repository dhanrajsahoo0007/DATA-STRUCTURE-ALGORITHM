# Question 
# Given an input array where the numbers range between 1 to n 
# They are not sorted 
# the array contains a duplicate and has a missing element 
# return the missing element and duplicate element  other wise return [-1,-1]

## Approach 
# The try to sort the element of the array with Swap sort 
# The logic is element should be present on that index , if not wap the element to the array's element value index 
# also check if the current iterative element i and the index of input[i] is same then we found the duplicate and the missing number (with index value + 1)
# by doing so there will be a case where the swap 


input = [1,3,2,6,5,7,6]

def swap_sort(input):
    for i in range(len(input)-1 ):
        print(i)
        if input[i] !=i +1:
            print(input[i])
            if input[i] == input[input[i]-1]:
                return [input[i],i+1]
            temp = input[i]
            input[input[i]] == input[i]
            input[i] == temp
    return [-1,-1]

print(swap_sort(input))