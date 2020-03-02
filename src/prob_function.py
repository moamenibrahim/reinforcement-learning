import pandas as pd
import numpy as np


def probability(bin_x, bin_y, state_x, state_y, throw_deg):
    # First throw exception rule if person is directly on top of bin:
    if((state_x == bin_x) & (state_y == bin_y)):
        probability = 1
    else:
        # To accomodate for going over the 0 degree line
        if((throw_deg > 270) & (state_x <= bin_x) & (state_y <= bin_y)):
            throw_deg = throw_deg - 360
        elif((throw_deg < 90) & (state_x > bin_x) & (state_y < bin_y)):
            throw_deg = 360 + throw_deg
        else:
            throw_deg = throw_deg

        # Calculate Euclidean distance
        distance = ((bin_x - state_x)**2 + (bin_y - state_y)**2)**0.5

        # max distance for bin will always be on of the 4 corner points:
        corner_x = [-10, -10, 10, 10]
        corner_y = [-10, 10, -10, 10]
        dist_table = pd.DataFrame()
        for corner in range(0, 4):
            dist = pd.DataFrame({'distance': (
                (bin_x - corner_x[corner])**2 + (bin_y - corner_y[corner])**2)**0.5}, index=[corner])
            dist_table = dist_table.append(dist)
        dist_table = dist_table.reset_index()
        dist_table = dist_table.sort_values('distance', ascending=False)
        max_dist = dist_table['distance'][0]

        distance_score = 1 - (distance/max_dist)

        # First if person is directly horizontal or vertical of bin:
        if((state_x == bin_x) & (state_y > bin_y)):
            direction = 180
        elif((state_x == bin_x) & (state_y < bin_y)):
            direction = 0

        elif((state_x > bin_x) & (state_y == bin_y)):
            direction = 270
        elif((state_x < bin_x) & (state_y == bin_y)):
            direction = 90

        # If person is north-east of bin:
        elif((state_x > bin_x) & (state_y > bin_y)):
            opp = abs(bin_x - state_x)
            adj = abs(bin_y - state_y)
            direction = 180 + np.degrees(np.arctan(opp/adj))

        # If person is south-east of bin:
        elif((state_x > bin_x) & (state_y < bin_y)):
            opp = abs(bin_y - state_y)
            adj = abs(bin_x - state_x)
            direction = 270 + np.degrees(np.arctan(opp/adj))

        # If person is south-west of bin:
        elif((state_x < bin_x) & (state_y < bin_y)):
            opp = abs(bin_x - state_x)
            adj = abs(bin_y - state_y)
            direction = np.degrees(np.arctan(opp/adj))

        # If person is north-west of bin:
        elif((state_x < bin_x) & (state_y > bin_y)):
            opp = abs(bin_y - state_y)
            adj = abs(bin_x - state_x)
            direction = 90 + np.degrees(np.arctan(opp/adj))

        direction_score = (45-abs(direction - throw_deg))/45

        probability = distance_score*direction_score
        if(probability > 0):
            probability = probability
        else:
            probability = 0

    return(probability)
