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


#  test
A = [1,7,8,9]
B = [0,4,5,6]
print(naive_sorting(merge(A,B)))