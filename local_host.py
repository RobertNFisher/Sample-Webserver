from bottle import route, run, response
from json_with_dates import dumps
from db_access import get_all_areas, get_categories_for_area, get_locations_for_area,\
    get_measurements_for_location, get_location, get_area
from db_utility import number_of_locations_by_area, get_average_measurements_for_area

# Creates paths for URL to run a report on the various areas and their measurements

# Gets all areas
@route('/measures/area')
def area():
    response.content_type = "application/json"
    data = get_all_areas()
    return dumps(data)

# Get select area
@route('/measures/area/<area_id:int>')
def area(area_id):
    response.content_type = "application/json"
    data = get_area(area_id)
    return dumps(data)

# Gets location for given index
@route('/measures/location/<loc_id:int>')
def location(loc_id):
    response.content_type = "application/json"
    data = get_location(loc_id)
    return dumps(data)

# gets location based off area
@route('/measures/area/location/<area_id:int>')
def location_area(area_id):
    data = get_locations_for_area(area_id)
    response.content_type = "application/json"
    return dumps(data)

# gets measurements for are based off of location ID
@route('/measures/location/measurements/<location_id:int>')
def measurements_in_location(location_id):
    response.content_type = "application/json"
    data = get_measurements_for_location(location_id)
    return dumps(data)

# gets all categories for that area
@route('/measures/area/category/<area_id:int>')
def categories_in_area(area_id):
    response.content_type = "application/json"
    data = get_categories_for_area(area_id)
    return dumps(data)

# gets the locations for given area
@route('/measures/area/location/total/<area_id:int>')
def locations_by_area(area_id):
    response.content_type = "application/json"
    data = number_of_locations_by_area(area_id)
    return dumps(data)

# returns the average measurements taken for given area
@route('/measures/area/average/<area_id:int>')
def average_measurements(area_id):
    response.content_type = "application/json"
    data = get_average_measurements_for_area(area_id)
    return dumps(data)

run(host='localhost', port=21212, debug=True)
