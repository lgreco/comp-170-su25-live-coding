def naive_sorting(our_data: list[int]):
    # Consider a progressively decreasing version of
    # our input array
    for end in range(len(our_data) - 1, 1, -1):
        # Find the largest element in this version of the array
        # Assume largest is the first element
        largest = 0
        for i in range(1, end + 1):
            if our_data[i] > our_data[largest]:
                largest = i
        # When the loop ends, largest points to the largest
        # element in range 0...end-1. Place the largest element
        # at position end-1 and whatever was at position end-1
        # at position largest
        temp = our_data[largest]
        our_data[largest] = our_data[end - 1]
        our_data[end - 1] = temp
