def naive_sorting(our_data: list[int]):
    # Consider a progressively decreasing version of
    # our input array
    for end in range(len(our_data), 1, -1):
        # Find the largest element in this version of the array
        # Assume largest is the first element
        largest = 0
        for i in range(1, end):
            if our_data[i] > our_data[largest]:
                largest = i
        # When the loop ends, largest points to the largest
        # element in range 0...end-1. Place the largest element
        # at position end-1 and whatever was at position end-1
        # at position largest
        temp = our_data[largest]
        our_data[largest] = our_data[end - 1]
        our_data[end - 1] = temp
    return our_data

def merge(A:list[int], B:list[int]) -> list[int]:
    # Leftmost pointers for lists A and B
    i = j = 0
    # Output list
    C = list()
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1
    while i < len(A):
        C.append(A[i])
        i += 1
    while j < len(B):
        C.append(B[j])
        j += 1
    return C

def merge_sort(array:list[int]) -> list[int]:
    result = list()
    if len(array) == 1:
        result.append(array[0])
    else:
        # Split input array in half
        mid = len(array) // 2
        left = list()
        right = list()
        for i in range(mid):
            left.append(array[i])
        for i in range(mid,len(array)):
            right.append(array[i])
        try_again_left = merge_sort(left)
        try_again_right = merge_sort(right)
        result = merge(try_again_left, try_again_right)
    return result


# test 
array = [5,1,6,2,8,4,7,3]
sorted_array = merge_sort(array)
print(sorted_array)