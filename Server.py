import requests
from bottle import route, run, request, static_file, SimpleTemplate
import json_with_dates
from json import loads

WEB_PORT = 8000

# Handles displaying an error page whenever a user attempts to send an invalid result
def error(messages):
    template = SimpleTemplate(name="error_page.html", lookup=["templates"])
    page = template.render(messages=messages)
    return page


# Homepage for Measures website
@route('/')
def album_list():
    # returns a list of areas and lads it
    r = requests.get("http://localhost:21212/measures/area")
    a_list = loads(r.text)
    # sets the page to the .html file area_select.html
    template = SimpleTemplate(name="area_select.html", lookup=["templates"])
    page = template.render(area_list=a_list)
    return page

# Called from home page when an area is selected for querey
@route('/area_info')
def area_info():
    # Grabs the selected area id
    area_id = request.query.getall("area-select")

    # if there are more than one area id, return error page
    if len(area_id) != 1:
        return error("Must provide exactly one area\n"
              "you provided {}".format(len(area_id)))
    else:
        # grab given area id from list
        area_id = area_id[0]
        r = requests.get("http://localhost:21212/measures/area/location/{}".format(area_id))
        # if not accepted, pass error and error code
        if r.status_code != 200:
            return error(["Error in REST Server",
                          "status code is {}".format(r.status_code)])
        # Otherwise continue gathering the rest of the required information from localhost
        else:
            # gathers the area's location
            r = requests.get("http://localhost:21212/measures/area")
            area_info = loads(r.text)
            info = area_info[int(area_id)-1]

            # gathers the location information given the current area
            r = requests.get("http://localhost:21212/measures/area/location/{}".format(area_id))
            locations = loads(r.text)

            # collects the average measurements of the given area
            r = requests.get("http://localhost:21212/measures/area/average/{}".format(area_id[0]))
            avg_measure = loads(r.text)

            # calls the html file that handles area info
            template = SimpleTemplate(name="area_information.html", lookup=["templates"])

            return template.render(a_name=info[1], area_id=info[0], lon=info[2], lat=info[3], a_measure=avg_measure,
                                   locations=locations)

@route('/location_info')
def location_info():
    # Grabs the selected location id
    loc_id = request.query.getall("location_selected")

    # if there are more than one area id, return error page
    if len(loc_id) != 1:
        return error("Must provide exactly one area\n"
                     "you provided {}".format(len(loc_id)))
    else:
        # set loc_id
        loc_id = loc_id[0]
        # request location information
        r = requests.get('http://localhost:21212/measures/location/{}'.format(loc_id))
        loc_info = loads(r.text)
        loc_info = loc_info[0]

        # request area information for name
        r = requests.get("http://localhost:21212/measures/area/{}".format(loc_info[3]))
        area_name = loads(r.text)
        area_id = area_name[0][0]
        area_name = area_name[0][1]

        # request measurements for location for count and avg
        r = requests.get("http://localhost:21212/measures/location/measurements/{}".format(loc_id))
        measurements = loads(r.text)
        measure_count = measurements.__len__()

        if measure_count != 0:
            # calculate avg measurement
            avg = 0
            for measure in measurements:
                avg += measure[1]

            avg /= measure_count

        else:
            avg = "N/A"

        # render html
        template = SimpleTemplate(name="Location_Information.html", lookup=["templates"])

        return template.render(loc_name=loc_info[1], loc_id=loc_id, altitude= loc_info[2], area_name= area_name,
                               count= measure_count, avg= avg, measurements= measurements, area_id= area_id)



run(host="localhost", port=WEB_PORT)