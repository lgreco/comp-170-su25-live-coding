# Same data as in JUN16-bad-code.py file, only neatly organized as a list
daily_highs = [75, 77, 68, 65, 71, 78, 73, 56, 66, 68, 65, 83, 84, 78]

def average(values: list[int]) -> int:
    """Basic function that averages the values in a given list
    
    Input
    -----
    values : list
      values to average - must be numeric data
    
    Returns
    -------
    The average of the values entered.
    """
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
average_daily_high = average(daily_highs)
# Plain printing
print(average_daily_high)
# Fancy printing
print(f"{average_daily_high:.1f}")


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

# Simple demo
print(f"The smallest daily high temperatue is {find_min(daily_highs)}")