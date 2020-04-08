## @file pos_adt.py
#  @author Bruce He
#  @brief module that implements and an ADT for global position coordinates and calculations around it
#  @date 2020/1/15

from math import *
from date_adt import *

# @@ brief create ADT for position coordinates related calculation
class GPosT:

    ## @brief GPosT constructor
    #  @detail initialized GPosT object with inputs latitude and longitude.
    #          This module expect users to input reasonable latitude in range of [-90, 90],
    #          and longitude in range of [-180,180].
    #  @param lat corresponds to the latitude, positive lat is North, negative lat is South
    #  @param long corresponds to the longitude, positive long is Ease, negative long is West
    #  @exception ValueError shows if latitude or longitude is out or range.
    def __init__(self, lat, long):
        if lat > 90 or lat < -90 or long > 180 or lat < -180:
            raise ValueError("Value Out of range")
        self.__lat = lat
        self.__long = long

    ## @brief getter for latitude
    # @return the value of latitude
    def lat(self):
        return self.__lat

    ## @brief getter for longitude
    #  @return the value of longitude
    def long(self):
        return self.__long

    ## @brief determine if current position is West of p
    #  @detail Compare the value of longitude of current position to GPostT p. If longitude of current position is smaller,
    #          then it is West of p, so return True. Return False otherwise.
    #          One thing worth noticing is: float lose precision when the difference is small.
    #  @return True if the current position is West of p; False otherwise
    def west_of(self, p):
        if self.long() < p.long():
            return True
        else:
            return False

    ## @brief determine if current position is North of p
    #  @detail Compare the value of latitude of current position to GPostT p. If latitude of current position is larger,
    #          then it is North of p, so return True. Return False otherwise.
    #          One thing worth noticing is: float lose precision when the difference is small.
    #  @param p GPosT object with latitude and longitude
    #  @return True if the current position is North of p; False otherwise
    def north_of(self, p):
        if self.lat() > p.lat():
            return True
        else:
            return False

    ## @brief determine the distance between current position and argument p(in km)
    #  @detail Followed by the instruction, 'haversine' formula is used directly
    #          to calculate the distance between two points.
    #  @param p GPosT object with latitude and longitude
    #  @param radius Earth's mean radius
    #  @param lat1 latitude of current position in radians
    #  @param lat2 latitude of position p in radians
    #  @param lat_delta difference of latitude between current position and position p, in radians
    #  @param long_delta difference of longitude between current position and position p, in radians
    #  @param a square of half the chord length between 2 points
    #  @param c the angular distance in radians
    #  @return the distance between current position and p with unit of km
    def distance(self, p):
        radius = 6371
        lat1 = radians(self.lat())
        lat2 = radians(p.lat())
        lat_delta = lat1 - lat2
        long_delta = radians(self.long()) - radians(p.long())
        a = sin(lat_delta/2)**2 + cos(lat1) * cos(lat2) * sin(long_delta/2)**2
        c = 2 * atan2(sqrt(a), sqrt(1-a))
        return radius * c

    ## @brief determine whether current position is the same as position p
    #  @detail use self.distance(p) to get value of distance between current position and position p.
    #          Followed by instruction, if the value is less than 1, that means two positions are considered equal.
    #  @param p GPosT object with latitude and longitude
    #  @return True if 2 points are within 1 km; False otherwise.
    def equal(self, p):
        if self.distance(p) <= 1:
            return True
        else:
            return False

    ## @brief change current position with bearing b and distance d
    #  @detail With the formula provide in https://www.movable-type.co.uk/scripts/latlong.html,
    #          use current position, bearing and distance to calculate the moved position
    #  @param b the value of bearing
    #  @param d distance moved in unit of km
    #  @param ang angular distance, calculated by d/r; d is distance moved, r is Earth's mean radius
    #  @param rad_lat latitude of current position in radians
    #  @param rad_long longitude of current position in radians
    #  @param new_lat latitude of moved position in radians
    #  @param new_long longitude of moved position in radians
    def move(self, b, d):
        ang = d/6371
        bearing = radians(b)
        rad_lat = radians(self.lat())
        rad_long = radians(self.long())
        new_lat = asin(sin(rad_lat) * cos(ang) + cos(rad_lat) * sin(ang) * cos(bearing))
        new_long = rad_long + atan2(sin(bearing) * sin(ang) * cos(rad_lat), cos(ang) - sin(rad_lat) * sin(new_lat))
        self.__lat = degrees(new_lat)    # update the latitude in degree type
        self.__long = degrees(new_long)  # update the longitude in degree type

    ## @brief return DateT object that shows arrival date
    #  @detail start at date d, moving from current position to position p at a speed s.
    #          Since DateT.add_days(n) will round off to 1 days if n = 1.9, so the day used for moving from current position
    #          to point p will round up. If n = 1.9, the actual day used is 2 days.
    #  @param p target position in GPosT type
    #  @param s speed with units km/day
    #  @param d starting date in DateT type
    #  @param distance the distance between current position and position p, in unit of km
    #  @param day_used day used to finish the trip with speed s, rounding up
    #  @return the arrival date
    def arrival_date(self, p, d, s):
        distance = self.distance(p)
        day_used = ceil(distance/s)
        return d.add_days(day_used)

















