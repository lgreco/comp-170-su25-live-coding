# obtain height
N = int(input("\nHow many lines tall do you want the tower? "))
print()

# The aspect ratio of the Sears Tower 1:6.45 based on Chicago Architectural 
# Foundation. In other words, the tower is 6.45 times taller than wide
ASPECT_RATIO = 6.45 

# The tower has actually four tiers but for simplicity we assume there are
# three tiers, each occupying the following proportons of the total height
BOTTOM_TIER_PROPORTION = 0.50 # based on actual
MIDDLE_TIER_PROPORTION = 0.35 # measurements and
TOP_TIER_PROPORTION = 0.15    # omitting one setback

# These are the setback transitions for the three tiers of our tower
BOTTOM_TO_MIDDLE_SETBACK = 0.66
MIDDLE_TO_TOP_SETBACK = 0.75

# Compute the dimensions for bottom block
bottom_width = N / ASPECT_RATIO # height/aspect ratio
bottom_height = N * BOTTOM_TIER_PROPORTION

# Compute the dimensions for middle block
middle_width = BOTTOM_TO_MIDDLE_SETBACK * bottom_width
middle_height = N*MIDDLE_TIER_PROPORTION

# Compute the dimensions for top block
top_width = MIDDLE_TO_TOP_SETBACK * middle_width
top_height = N*TOP_TIER_PROPORTION