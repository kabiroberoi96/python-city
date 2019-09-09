def draw_firestation(no_building):
    #testing GutHub
    
    # building supplies aka variables
    roof = "----"
    pillars = "|  |"
    floor = "----"

    if no_building < 0:
        raise ValueError("Number of buildings must be positive")

    else:
    #print("fire station found")
        print(roof*no_building)
        print(pillars*no_building)
        print(floor*no_building)

    return

draw_firestation(2)
