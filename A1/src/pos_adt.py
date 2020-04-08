## @file pos_adt.py
#  @author Dhruv Bhavsar
#  @brief An abstract date type for global position coordinates and allows for several functions on them
#  @date Jan 16 2020

import math
from date_adt import DateT

## @brief An ADT that represents global position coordinates
class GPosT:

    ## @brief Constructor that creates a new GPosT object with latitude and longitude (in degrees)
    #  @details First check if latitude and longitude are in range then save them to the class variables else throw
    #  value error
    #  @param latitude and longitude (in degrees) are real numbers
    def __init__(self, latitude, longitude):
        if not -90 <= latitude <= 90:
            raise ValueError("Latitude must be in -90..90")
        if not -180 <= longitude <= 180:
            raise ValueError("Longitube must be in -180..180")

        self.latitude = latitude
        self.longitude = longitude

    ## @brief Getter for latitude
    #  @return the latitude as a double
    def lat(self):
        return self.latitude

    ## @brief Getter for longitude
    #  @return the longitude as a double
    def long(self):
        return self.longitude
    ## @brief Checks if current position is west of parameter position
    #  @details
    #  @param p - GPosT object which you are comparing with
    #  @return True if the current position is west of parameter position else False
    def west_of(self, p):
        return self.longitude < p.longitude

    ## @brief Checks if current position is north of parameter position
    #  @details
    #  @param p - GPosT object which you are comparing with
    #  @return True if the current position is north of parameter position else False
    def north_of(self, p):
        return self.latitude > p.latitude

    ## @brief Checks if the distance is equal by calculating the distance
    #  @details Using the formula provided in specifications https://www.movable-type.co.uk/scripts/latlong.html
    #  @param p - GPosT object comparing with
    #  @return True if the distance is less than 1 km else False
    def equal(self, p):
        radius = 6371
        lat = math.radians(self.latitude)
        lat2 = math.radians(p.latitude)

        lat_diff = math.radians(p.latitude - self.latitude)
        long_diff = math.radians(p.longitude - self.longitude)

        a = math.sin(lat_diff/2) * math.sin(lat_diff/2) + math.cos(lat) * math.cos(lat2) \
            * math.sin(long_diff/2) * math.sin(long_diff/2)

        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

        distance = radius * c

        return distance < 1

    ## @brief Moves the current object d (km) towards b (bearing)
    #  @details Using the formula provided in the specifications https://www.movable-type.co.uk/scripts/latlong.html
    #           under Destination point given distance and bearing from start point then the new position gets updated
    #           to be the current. Firstly convert all degrees into radians as the formula requires radians. Also I
    #           check if the new positions are greater than their ranges, if so then I apply a formula to normalize them
    #           which can be found from the website given in the specifications
    #           https://www.movable-type.co.uk/scripts/latlong.html
    #  @param b - bearing type real and d - distance in km type real
    def move(self, b, d):
        radius = 6371
        rad_lat = math.radians(self.latitude)
        rad_long = math.radians(self.longitude)
        rad_bearing = math.radians(b)

        self.latitude = math.asin(math.sin(rad_lat) * math.cos(d / radius)
                                  + math.cos(rad_lat) * math.sin(d / radius) * math.cos(rad_bearing))

        self.longitude = rad_long + math.atan2(math.sin(rad_bearing) * math.sin(d / radius) * math.cos(rad_lat),
                                               math.cos(d / radius) - math.sin(rad_lat) * math.sin(self.latitude))
        new_lat = math.degrees(self.latitude)
        new_long = math.degrees(self.longitude)
        self.latitude = new_lat if abs(new_lat) < 90 else (new_lat + 270) % 180 - 90
        self.longitude = new_long if abs(new_long) < 180 else (new_long + 540) % 360 - 180

    ## @brief Calculate the distance between current position and position p
    #  @details Using the formula provided in the specifications https://www.movable-type.co.uk/scripts/latlong.html
    #           under Distance
    #  @param p - GPosT object that we are finding the distance between
    #  @return the distance in kilometers between the two positions
    def distance(self, p):
        radius = 6371
        lat = math.radians(self.latitude)
        lat2 = math.radians(p.latitude)

        lat_diff = math.radians(p.latitude - self.latitude)
        long_diff = math.radians(p.longitude - self.longitude)

        a = math.sin(lat_diff/2) * math.sin(lat_diff/2) + math.cos(lat) * math.cos(lat2) \
            * math.sin(long_diff/2) * math.sin(long_diff/2)

        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

        return radius * c

    ## @brief Calculate the arrival date starting from the current position and traveling towards position p at s
    #         kilometers per day
    #  @details First calculate the distance between current position and desired position (p), then divide the distance
    #           by s to get days it takes to reach that position. Finally use the DateT method add_days to add the days
    #           needed to travel the distance. The reason I took the ceil of days is because I want to give the date
    #           that they will reach the position by. Also, it doesnt make sense to input a negative speed in this case.
    #  @param p - GPosT object that we need to find the distance between, d - distance in km, s - speed in km/day
    #  @return a new DateT object that represents when the arrival date is
    def arrival_date(self, p, d, s):
        distance = self.distance(p)
        days = distance / s
        return d.add_days(math.ceil(days))
