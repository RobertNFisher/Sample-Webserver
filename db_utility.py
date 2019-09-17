from db_access import get_locations_for_area, get_measurements_for_location, get_all_areas, get_categories_for_area


def get_average_measurements_for_area(area_id):
    """
    Returns the average value of all measurements for all locations in the given area
    Returns None if there are no measurements.
    """
    # create a list of tuples containing the area to be measured
    locations = get_locations_for_area(area_id)

    # utility variables
    total = 0
    counter = 0
    # Loops through locations and adds the measurements for eah location to a total
    for row in locations:
        location_id = row[0]
        # Gets the measurement
        measurements = get_measurements_for_location(location_id)
        for col in measurements:
            # Adds measure to total
            total += col[1]
            # Counts number of locations
            counter += 1
    # Checks to see if there is no values
    if total != 0:
        return total / counter
    else:
        return None


def number_of_locations_by_area(area_id):
    """
    Returns the number of locations for the given area.
    """
    # gets the locations
    locations = get_locations_for_area(area_id)

    # counts the total number of locations
    counter = 0
    for row in locations:
        counter += 1

    # Returns the total amount
    return counter
