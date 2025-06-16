# Average high temperature for last week
def naive_average():
    mon1 = 75
    tue1 = 77
    wed1 = 68
    thu1 = 65
    fri1 = 71
    sat1 = 78
    sun1 = 73

    mon2 = 56
    tue2 = 66
    wed2 = 68
    thu2 = 65
    fri2 = 83
    sat2 = 84
    sun2 = 78

    sum = mon1 + tue1 + wed1 + thu1 + fri1 + sat1 + sun1 + mon2 + tue2 + wed2 + thu2 + fri2 + sat2 + sun2

    avg = sum/14

    print(f"\n\nThe average temperature is {avg:.1f}\n\n")


daily_highs = [75, 77, 68, 65, 71, 78, 73, 56, 66, 68, 65, 83, 84, 78]

def standard_average(list_of_data):
    sum = 0
    """for temp in list_of_data:
        sum = sum + temp
    """
    # Traditional/legacy way to traverse an array
    for i in range(len(list_of_data)):
        temp = list_of_data[i]
        sum = sum + temp

    avg = sum/len(list_of_data)
    return av

def find_min(list_of_data):
    smallest = list_of_data[0]
    for i in range(1, len(list_of_data)):
        if list_of_data[i] < smallest:
            smallest = list_of_data[i]
    return smallest

print(find_min(daily_highs))