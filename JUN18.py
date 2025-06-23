# a simple string array

zoom_call = ["Kofi", "Leo", "Lula", "Lillie", "Elizabeth", "Emmanuel", "Ben", "Delaney", "Heather", "Omar"]

middle_of_array = len(zoom_call) // 2

print(middle_of_array)

print("Middle element of array: " + zoom_call[middle_of_array])

left_half = zoom_call[0:middle_of_array]
right_half = zoom_call[middle_of_array:len(zoom_call)]

print(f"{left_half=}")
print(f"{right_half=}")

simplified_left_half = zoom_call[:middle_of_array]
simplified_right_half = zoom_call[middle_of_array:]

print(f"{simplified_left_half=}\n{simplified_right_half=}")