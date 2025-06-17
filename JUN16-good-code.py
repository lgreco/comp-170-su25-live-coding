# Same data as in JUN16-bad-code.py file, only neatly organized as a list
daily_highs = [75, 77, 68, 65, 71, 78, 73, 56, 66, 68, 65, 83, 84, 78]

def average(values: list[int]) -> int:
    """Basic function that averages the values in a given list
    
    Input
    -----
    values : list
      values to average - must be numeric data. Dear user, please please please
      make sure that the list is not empty.
    
    Returns
    -------
    The average of the values entered.
    """

    # initialize average to None
    avg = None
    
    if len(values) > 0:
        
      # Initialize the sum accumulator
      sum = 0
      
      # Iterate the list (traverse it one element at a time from beginning to end)
      # and add its values together.      ALTERNATIVELY, with ENHANCED-FOR loop:
      for i in range(len(values)):        # for val in values:
          sum = sum + values[i]           #     sum = sum + val

      # Loop completed, compute average by dividing sum computed in the loop with
      # the number of values -- that's the length of the array. This operation
      # can be risky. Why? 
      avg = sum / len(values)

    # Done. Return the average value
    return avg

# Simple demo
# average_daily_high = average(daily_highs)
# Plain printing
# print(average_daily_high)
# Fancy printing
# print(f"{average_daily_high:.1f}")


def find_min(values: list[int]) -> int:
    """Basic technique to find the smallest item in an list.
    
    Input
    -----
    values : list
      values to search - must be numeric data
    
    Returns
    -------
    The smallest of the values entered. 
    """
    # Assume that the first item in the list is the smallest
    smallest = values[0]

    # Check every remaining item in the list if they are smaller than the
    # smallest value. When a smaller item is found, update the smallest
    # value to match. Loop stars from second element [i=1]. Why?
    #
    for i in range(1, len(values)):  # also:  for val in values:
        if values[i] < smallest:     #          if val < smallest:
            smallest = values[i]     #            smallest = val
    
    # Done
    return smallest

def find_max(values: list[int]) -> int:
    """Basic technique to find the largest item in an list. 
    This method uses a WHILE loop to demonstreate its equivalence
    to an exhaustive FOR loop
    
    Input
    -----
    values : list
      values to search - must be numeric data
    
    Returns
    -------
    The largest of the values entered. 
    """
    # Assume that the first item in the list is the largest
    
    i = 0
    largest = values[i]

    # Check every remaining item in the list if they are smaller than the
    # largest value. When a smaller item is found, update the largest
    # value to match. Loop stars from second element [i=1]. Why?
    while i < len(values):
        if values[i] > largest:
            largest = values[i]
        i = i+1
    
    # Done
    return largest

def exists(value: int, values: list[int]) -> bool:
    """
    for i in range(len(values)):
        if values[i] == value:
            return True
    return False
    """
    # Assume that the item is not present in the array
    found = False
    for val in values:
        if val == value:
            found = True
            break
    return found

demo = [1,2,3]
print(find_max(demo))