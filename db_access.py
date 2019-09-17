# Robert Fisher
# 01/31/2019
# Internet Programing


import sqlite3


def get_location(loc_id):
    """
    Returns a list of tuples representing all the rows in the
    location table
    """
    # Establish connection with the databse
    conn = sqlite3.connect("measures.sqlite")
    try:
        # Creates Cursor
        crs = conn.cursor()
        # Selects all information from location table
        cmd = "select * from location WHERE location_id = ?"
        crs.execute(cmd, [loc_id])
        # returns table as tuples

        return crs.fetchall()

    finally:
        conn.close()


def get_all_areas():
    """
    Returns a list of tuples representing all the rows in the
    area table.
    """
    # Establish a connection with the 'measures' database
    conn = sqlite3.connect("measures.sqlite")
    try:
        # Create a cursor to pull information
        crs = conn.cursor()
        # SQL command to pull the whole 'area' table
        cmd = "select * from area"
        crs.execute(cmd)

        return crs.fetchall()
    # close the connection to the database
    finally:
        conn.close()

def get_area(area_id):
    """
    Returns a list of tuples representing all the rows in the
    area table.
    """
    # Establish a connection with the 'measures' database
    conn = sqlite3.connect("measures.sqlite")
    try:
        # Create a cursor to pull information
        crs = conn.cursor()
        # SQL command to pull the whole 'area' table
        cmd = "select * from area WHERE area_id = ?"
        crs.execute(cmd, [area_id])

        return crs.fetchall()
    # close the connection to the database
    finally:
        conn.close()

def get_locations_for_area(area_id):
    """
    Return a list of tuples giving the locations for the given area.
    """
    # Establish a connection to the 'measures' database
    conn = sqlite3.connect("measures.sqlite")
    try:
        # Creates a cursor to pull the locations
        crs = conn.cursor()
        # SQL to pull eveything from location where location area = area id
        cmd = "select * from location WHERE location_area = ?"
        crs.execute(cmd, [area_id])

        return crs.fetchall()


    finally:
        conn.close()
        # Returns the results


def get_measurements_for_location(location_id):
    """
    Return a list of tuples giving the measurement rows for the given location.
    """
    # Establish a connection to the 'measures' database
    conn = sqlite3.connect("measures.sqlite")
    try:
        # Creates a cursor to pull from measurement
        crs = conn.cursor()
        # SQL to pull everything from measurements where measurement_location = location_id
        cmd = "select * from measurement WHERE measurement_location = ?"
        crs.execute(cmd, [location_id])
        return crs.fetchall()

    finally:
        conn.close()


def get_categories_for_area(area_id):
    """
    Return a list of rows from the category table that all contain the given area.
    """
    cat_list = []
    # Establishes connection to 'measures'
    conn = sqlite3.connect("measures.sqlite")
    try:
        # Creates a cursor to pull from category_area
        crs = conn.cursor()
        # SQL to pull everything from category_area where area_id = area_id
        cmd = "select * from category_area WHERE area_id = ?"
        crs.execute(cmd, [area_id])
        # Create a table with the crs command list
        table = crs.fetchall()

        # Looping through these results, searching for results where category_id = category_id
        for row in table:
            # Saves the category_id from 'category_area' table
            category_id = row[0]
            crs2 = conn.cursor()
            # SQL that pulls everything from category where category_id = category_id
            cmd2 = "select * from category WHERE category_id = ?"
            crs2.execute(cmd2, [category_id])
            # Store each category in a category list
            cat_list.append(crs2.fetchall()[0][1])

        # return the list
        return cat_list

    finally:
        conn.close()
