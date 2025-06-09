# Ask user about desired height
N = input("How tall should the tower be? ")
# Python's input returns the answer as a string; convert it to an integer number
N = int(N)
# Acknoledge the entry
print(f"Thank you. I'll parameterize the tower for {N} lines height.")

# The aspect ratio of the Sears Tower 1:6.45 based on Chicago Architectural 
# Foundation. In other words, the tower is 6.45 times taller than wide
ASPECT_RATIO = 1/6.45 

# The tower has actually four tiers but for simplicity we assume there are
# three tiers, each occupying the following proportons of the total height
BOTTOM_TIER_PROPORTION = 0.50 # based on actual
MIDDLE_TIER_PROPORTION = 0.35 # measurements and
TOP_TIER_PROPORTION = 0.15    # omitting one setback

# These are the setback transitions for the three tiers of our tower
BOTTOM_TO_MIDDLE_SETBACK = 0.33
MIDDLE_TO_TOP_SETBACK = 0.25

# Time to compute the dimensions for each block in the tower

# Bottom block

WIDTH_BOTTOM_TIER = N / ASPECT_RATIO # height/aspect ratio
HEIGHT_BOTTOM_TIER = N * BOTTOM_TIER_PROPORTION
print(f"\nThe bottom tier is {WIDTH_BOTTOM_TIER} characters wide and {HEIGHT_BOTTOM_TIER} lines tall")

# Middle block

WIDTH_MIDDLE_TIER = BOTTOM_TO_MIDDLE_SETBACK * WIDTH_BOTTOM_TIER 
HEIGHT_MIDDLE_TIER = N*MIDDLE_TIER_PROPORTION
print(f"\nThe middle tier is {WIDTH_MIDDLE_TIER} characters wide and {HEIGHT_MIDDLE_TIER} lines tall")

# Top block

WIDTH_TOP_TIER = MIDDLE_TO_TOP_SETBACK * WIDTH_MIDDLE_TIER
HEIGHT_TOP_TIER = N*TOP_TIER_PROPORTION
print(f"\nThe top tier is {WIDTH_TOP_TIER} characters wide and {HEIGHT_TOP_TIER} lines tall")