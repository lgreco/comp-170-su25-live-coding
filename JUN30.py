# example with full path to file

with open("/workspaces/comp-170-su25-live-coding/demo_data/text_file.txt", "r") as leo_masterpiece:
    opening_from = leo_masterpiece.read()
    print(opening_from) # OK, maybe William Shakespeare helped a bit too.

# Same but better organized ... this time it counts lines instead of just printing them

path_to_file = "/workspaces/comp-170-su25-live-coding/demo_data/"
file_name =  "text_file.txt"
line_count = 0
with open(path_to_file + file_name) as richard3:
    for line in richard3:
        line_count += 1 
print(f"\n\nThere are {line_count} line(s) in file {file_name}.\n")

# Try a file in the same folder as our program
path_to_file = "./" # File system speak for "same folder"
file_name =  "README.md"
with open(path_to_file + file_name) as local_file:
    contents_of_local_file = local_file.read()
    print(f"\n\nContents of {file_name}:\n\n{contents_of_local_file}\n")