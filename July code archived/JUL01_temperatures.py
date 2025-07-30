# Where to find the file
path_to_file = "/workspaces/comp-170-su25-live-coding/data/"
file_name = "temperatures.txt" \

# initialize accumulator
temperature_average = 0
count = 0
# connect to the file
with open(path_to_file+file_name, "r") as our_data_file:
    for line in our_data_file:
        temperature = int(line)
        temperature_average += temperature
        count += 1

# Compute average and return
temperature_average /= count
print(f"\nThe temperature over a period of {count} days is {temperature_average:.2f}\n")

outliar_margin = 0.33
with open(path_to_file+file_name) as our_data_file:
    for line in our_data_file:
        value = float(line)
        if value < temperature_average*(1-outliar_margin) or value > temperature_average*(1+outliar_margin):
            print(f"\nOutliar: {value}")