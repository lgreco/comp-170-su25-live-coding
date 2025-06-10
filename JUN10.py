def draw_block(width: int, height: int, fill_char: str) -> None:
    for i in range(height):
        print(fill_char * width)

def sears() -> None:
    # obtain height
    N = int(input("\nHow many lines tall do you want the tower? "))
    fill_char = input("\nWhich symbol you want to use (default is #)? ")
    print()

    # Check if fill character has been entered
    fill_char = "#" if fill_char == "" else fill_char

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
    bottom_width = int(N / ASPECT_RATIO) # height/aspect ratio
    bottom_height = int(N * BOTTOM_TIER_PROPORTION)

    # Compute the dimensions for middle block
    middle_width = int( BOTTOM_TO_MIDDLE_SETBACK * bottom_width)
    middle_height = int(N*MIDDLE_TIER_PROPORTION)

    # Compute the dimensions for top block
    top_width = int(MIDDLE_TO_TOP_SETBACK * middle_width)
    top_height = int(N*TOP_TIER_PROPORTION)

    # Debugging report
    # print(f"\n   top (WxH): {top_width} x {top_height}")
    # print(f"middle (WxH): {middle_width} x {middle_height}")
    # print(f"bottom (WxH): {bottom_width} x {bottom_height}")

    draw_block(top_width,    top_height,    fill_char)
    draw_block(middle_width, middle_height, fill_char)
    draw_block(bottom_width, bottom_height, fill_char)


# To execute the program, just this:
sears()