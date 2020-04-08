## @file date_adt.py
#  @author Dhruv Bhavsar
#  @brief An abstract data type that represents Date and allows for other functions to manipulate Date
#  @date Jan 15 2020

import datetime

## @brief An ADT that represents Date
class DateT:



    ## @brief Constructor that inializes the object with year, month and day
    #  @details Using a try and except, the inputted date is tested with datetime to see if its valid then save them in
    #  class variables else raise error.
    #  @param m - Month, d - Day, y- Year
    def __init__(self, d, m, y):
      try:
        datetime.date(y, m, d)
        self.y = y
        self.d = d
        self.m = m
      except:
        raise


    ## @brief Getter for day
    #  @return The day as an int
    def day(self):
      return self.d


    ## @brief Getter for month
    # @return The month as an int
    def month(self):
      return self.m


    ## @brief Getter for year
    #  @return The year as an int
    def year(self):
      return self.y


    ## @brief Find the next day from the current object
    #  @details Create a datetime object with current object and use timedelta function to add one day and extract
    #           year, month and day
    #  @return DateT object of next day
    def next(self):
      cur_date = datetime.date(self.y, self.m, self.d)
      next_date = cur_date + datetime.timedelta(days=1)
      return DateT(next_date.day, next_date.month, next_date.year)


    ## @brief Find the day before current object
    #  @details Creates a datetime object with current object and use timedelta function to subtract one day and extract
    #           year, month, day
    #  @return DateT object of the previous day
    def prev(self):
      cur_date = datetime.date(self.y, self.m, self.d)
      prev_date = cur_date - datetime.timedelta(days=1)
      return DateT(prev_date.day, prev_date.month, prev_date.year)


    ## @brief Finds if the current date is before the d object
    #  @details Creates a datetime object with current object and a datetime object with the parameter d. Then compare the
    #           datetime objects
    #  @param d - DateT object to compare with
    #  @return True if the current object is before param d else False
    def before(self, d):
      cur_date = datetime.date(self.y, self.m, self.d)
      new_date = datetime.date(d.y, d.m, d.d)
      return cur_date < new_date    # Use less than since we want to find out if date is before


    ## @brief Finds if the current date is after the d object
    #  @details Creates a datetime object with current object and a datetime object with the parameter d. Then compare the
    #           datetime objects
    #  @param d - DateT object to compare with
    #  @return True if the current object is after param d else False
    def after(self, d):
      cur_date = datetime.date(self.y, self.m, self.d)
      new_date = datetime.date(d.y, d.m, d.d)
      return cur_date > new_date   # Use greater than since we want to find out if date is after


    ## @brief Checks if the dates are the same
    #  @details Compares the day, month and year among the two objects
    #  @param d - DateT object to compare with
    #  @return True if the date are the same else False
    def equal(self, d):
      return self.y == d.y and self.m == d.m and self.d == d.d


    ## @brief Adds n days to the current DateT object
    #  @details Creates a datetime object with the current object, then uses the timedelta function to add n days and
    #           finally extracts the year, month and day. If you enter a decimal number for n it will round to nearest
    #           whole number and then add those many days. Accepts negative days (to go back days)
    #  @param n - number of days to add on to the current date (int)
    #  @return a DateT object with the new date
    def add_days(self, n):
      cur_date = datetime.date(self.y, self.m, self.d)
      new_date = cur_date + datetime.timedelta(days=n)
      return DateT(new_date.day, new_date.month, new_date.year)


    ## @brief Find the days between the current object and parameter object
    #  @details Creates a datetime object with the current object and a datetime object with the parameter object. Then
    #           find the difference between the two dates by subtracting.
    #  @param d - DateT object find the difference in days from
    #  @return the absolute value of the difference since the user can enter a date that is before the current date
    def days_between(self, d):
      cur_date = datetime.date(self.y, self.m, self.d)
      new_date = datetime.date(d.y, d.m, d.d)
      return abs(new_date - cur_date).days



