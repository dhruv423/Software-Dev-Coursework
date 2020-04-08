## @file date_adt.py
# @author Bruce He
# @brief ADT for DateT
# @date 2020/01/14

from datetime import *


# @brief create ADT for date related calculation
class DateT:

    ## @brief DateT constructor
    #  @details initialize DateT object with integers d, m, y as input
    #           If any invalid input of dates is given, a ValueError will shown
    #  @param datetime represents current date in datetime type
    #  @param d correspond to day
    #  @param m correspond to month
    #  @param y correspond to year
    #  @exception ValueError throws when inputs are not valid for datetime
    def __init__(self, d, m, y):
        try:
            self.__datetime = datetime(y, m, d)
        except:
            raise ValueError("Please input valid datetime.")
        self.__d = d
        self.__m = m
        self.__y = y

    ## @brief shows the value of current day
    #  @return the value of current day
    def day(self):
        return self.__d

    ## @brief shows the value of current month
    #  @return the value of current month
    def month(self):
        return self.__m

    ## @brief shows the value of current year
    #  @return the value of current year
    def year(self):
        return self.__y

    ## @brief shows the day after current date
    #  @detail First create a datetime object 'add1date' by adding self.__datetime and timedelta(1),
    #          which represents 1 day. Then extract the values of new day, month and year by using Class Attributes.
    #          Finally, return a DateT object with the new date.
    #  @param add1date adding one day in current date
    #  @return DateT object that is one day later than current date
    def next(self):
        add1date = self.__datetime + timedelta(1)
        self.__d = add1date.day
        self.__m = add1date.month
        self.__y = add1date.year

        return DateT(self.__d, self.__m, self.__y)

    ## @brief shows the day before current date
    #  @detail With a similar to the next() method, prev() method instead return one day before current date.
    #  @param minus1date showing one day earlier than current date
    #  @return DateT object that is one day earlier than current date
    def prev(self):
        minus1date = self.__datetime + timedelta(-1)
        self.__d = minus1date.day
        self.__m = minus1date.month
        self.__y = minus1date.year

        return DateT(self.__d, self.__m, self.__y)

    ## @brief determine if current date is before the target date d
    #  @detail Transfer target date d as datetime type. Then, use diff to store the difference in days between
    #          current date and target date, in value of days.Then, convert diff from timedelta to integer.
    #          If diff is smaller than 0, current date is before target date, so return True. Return false otherwise.
    #  @param d target date for comparison
    #  @param temp_date represent target date
    #  @param diff value of difference between current date to target date, measured in days.
    #  @return True if current date is before target date, False otherwise.
    def before(self, d):
        temp_date = datetime(d.year(), d.month(), d.day())  # Use day() to get value of day, instead of d.day
        diff = self.__datetime - temp_date
        diff = diff.days
        if diff < 0:
            return True
        else:
            return False

    ## @brief determine if current date is after the target date d
    #  @detail Similar process as method before(self, d). This time, return true if diff is greater than 0, which means
    #          current date is after target date. Return False otherwise.
    #  @param d target date for comparison
    #  @param temp_date represent target date
    #  @param diff value of difference between current date to target date, measured in days.
    #  @return True if current date is after target date, False otherwise.
    def after(self, d):
        temp_date = datetime(d.year(), d.month(), d.day())
        diff = self.__datetime - temp_date
        diff = diff.days
        if diff > 0:
            return True
        else:
            return False

    ## @brief determine if current date is equal to the target date d
    #  @detail Similar process as method after(self, d) and before (self, d). This time, return true if diff is 0, which
    #          means current is the same as target date. Return False otherwise.
    #  @param d target date for comparison
    #  @param temp_date represent target date
    #  @param diff value of difference between current date to target date, measured in days.
    #  @return True if current date is the same as target date, False otherwise.
    def equal(self, d):
        temp_date = datetime(d.year(), d.month(), d.day())
        diff = self.__datetime - temp_date
        diff = diff.days
        if diff == 0:
            return True
        else:
            return False

    ## @brief take integer n, return DateT that is n days later than current date
    #  @detail Create a new datetime object new_date by adding current datetime with n days, in timedelta format.
    #          I assume that n can either be positive or negative. If n is positive, that means we want a new date that
    #          is n days after the current date. If n is negative, that means we want a new date that is n days earlier
    #          than current date. If n is zero, new date is the same as current date.
    #          Expect input n as integer with reasonable value.
    #  @param n days be added on current date
    #  @param new_date represents date to be shown, after calculation
    #  @return DateT object, with n days added or subtracted to the current date
    def add_days(self, n):
        new_date = self.__datetime + timedelta(n)
        return DateT(new_date.day, new_date.month, new_date.year)

    ## @brief take DateT object d, return the number of days between current date and date d
    #  @detail I assume that the number of difference in days, between two dates, is always non-negative.
    #          So no matter current date is before or after the date stored in d, the returning value is non-negative.
    #          First, transfer d from DateT object to datetime type, in new_date.
    #          Then, subtracting one date to another date, and change result from timedelta object to integer.
    #          Return the integer that represents the day difference between current date and date d.
    #  @param d DateT object used to compare with current date
    #  @param new_date represents date stored in DateT object d
    #  @return the number of days between current date and date stored in d
    def days_between(self, d):
        new_date = datetime(d.year(), d.month(), d.day())
        if self.__datetime >= new_date:
            return (self.__datetime - new_date).days
        else:
            return (new_date - self.__datetime).days














