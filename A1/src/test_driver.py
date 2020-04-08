## @file test_driver.py
#  @author Dhruv Bhavsar
#  @brief Test cases for DateT and GPosT
#  @date Jan 19 2020

#  Reference for testing format:
#  https://gitlab.cas.mcmaster.ca/smiths/se2aa4_cs2me3/blob/master/Assignments/PreviousYears/2017/A1/A1Soln/src/testCircles.py

from date_adt import *
from pos_adt import *


date1 = DateT(28, 2, 2020)
date2 = DateT(3, 4, 1983)
date3 = DateT(29, 2, 2020)
date4 = DateT(22, 7, 2022)
date5 = DateT(1, 1, 2019)
date6 = DateT(31, 12, 2005)
date7 = DateT(23, 4, 2000)
date8 = DateT(29, 7, 1988)
date9 = DateT(1, 3, 2004)
date10 = DateT(22, 7, 2022)



def test_day():
    global test_total, passed
    test_total += 1
    try:
        try:
            date_invalid = DateT(29, 2, 2019)
            print("invalid DateT test FAILED")
        except ValueError:
            print("invalid DateT test PASSED")
        assert date1.day() == 28
        assert date2.day() == 3
        assert date3.day() == 29
        assert date4.day() == 22
        assert date5.day() == 1
        passed += 1
        print("day test PASSED")
    except AssertionError:
        print("day test FAILED")


def test_month():
    global test_total, passed
    test_total += 1
    try:
        assert date6.month() == 12
        assert date7.month() == 4
        assert date8.month() == 7
        assert date1.month() == 2
        passed += 1
        print("month test PASSED")
    except AssertionError:
        print("month test FAILED")


def test_year():
    global test_total, passed
    test_total += 1
    try:
        assert date1.year() == 2020
        assert date2.year() == 1983
        assert date8.year() == 1988
        passed += 1
        print("year test PASSED")
    except AssertionError:
        print("year test FAILED")


def test_next():
    global test_total, passed
    test_total += 1
    try:
        next_date = date1.next()
        assert next_date.day() == 29 and next_date.month() == 2 and next_date.year() == 2020
        next_date = date3.next()
        assert next_date.day() == 1 and next_date.month() == 3 and next_date.year() == 2020
        next_date = date6.next()
        assert next_date.day() == 1 and next_date.month() == 1 and next_date.year() == 2006
        passed += 1
        print("next test PASSED")
    except AssertionError:
        print("next test FAILED")


def test_previous():
    global test_total, passed
    test_total += 1
    try:
        prev_date = date5.prev()
        assert prev_date.day() == 31 and prev_date.month() == 12 and prev_date.year() == 2018
        prev_date = date9.prev()
        assert prev_date.day() == 29 and prev_date.month() == 2 and prev_date.year() == 2004
        prev_date = date7.prev()
        assert prev_date.day() == 22 and prev_date.month() == 4 and prev_date.year() == 2000
        new_date = date1.add_days(-365)
        passed += 1
        print("previous test PASSED")
    except AssertionError:
        print("previous test FAILED")


def test_before():
    global test_total, passed
    test_total += 1
    try:
        assert date2.before(date1)
        assert date1.before(date2) == False
        assert date1.before(date3)
        passed += 1
        print("before test PASSED")
    except AssertionError:
        print("before test FAILED")


def test_after():
    global test_total, passed
    test_total += 1
    try:
        assert date1.after(date2)
        assert date8.after(date7) == False
        assert date5.after(date2)
        passed += 1
        print("after test PASSED")
    except AssertionError:
        print("after test FAILED")


def test_equal():
    global test_total, passed
    test_total += 1
    try:
        assert date10.equal(date4)
        assert date5.equal(date6) == False
        passed += 1
        print("equal test PASSED")
    except AssertionError:
        print("equal test FAILED")


def test_add_days():
    global test_total, passed
    test_total += 1
    try:
        new_date = date1.add_days(365)
        assert new_date.day() == 27 and new_date.month() == 2 and new_date.year() == 2021
        new_date = date1.add_days(-365)
        assert new_date.day() == 28 and new_date.month() == 2 and new_date.year() == 2019
        new_date = date9.add_days(30)
        assert new_date.day() == 31 and new_date.month() == 3 and new_date.year() == 2004
        passed += 1
        print("add days test PASSED")
    except AssertionError:
        print("add days test FAILED")


def test_days_between():
    global test_total, passed
    test_total += 1
    try:
        assert date5.days_between(date5) == 0
        assert date1.days_between(date7) == 7250
        assert date1.days_between(date3) == 1
        assert date6.days_between(date5) == 4749
        passed += 1
        print("days between test PASSED")
    except AssertionError:
        print("days between test FAILED")


test_total = 0
passed = 0


test_day()
test_month()
test_year()
test_next()
test_previous()
test_before()
test_after()
test_equal()
test_add_days()
test_days_between()

print(passed, "out of", test_total, "tests passed for DateT")
print("")

gpost1 = GPosT(0, 0)
gpost2 = GPosT(1, 4)
gpost3 = GPosT(-90, 0)
gpost4 = GPosT(90, 0)
gpost5 = GPosT(-45.435, 67.54)
gpost6 = GPosT(-90, 180)
gpost7 = GPosT(90, -180)
gpost8 = GPosT(-89.54, -179.534)
gpost9 = GPosT(23.566, 5.77)
gpost10 = GPosT(65.23, -137.99)
gpost11 = GPosT(23.566, 5.77)
gpost12 = GPosT(0, 0.007)


test_total = 0
passed = 0

def isClose(test_ans, actual_ans):
    # Gives errors up to 0.3% Source: https://www.movable-type.co.uk/scripts/latlong.html
    return abs(actual_ans - test_ans) <= actual_ans * 0.003




def test_lat():
    global test_total, passed
    test_total += 1
    try:
        try:
            invalid_gpost = GPosT(-56,-181)
            print("invalid GPosT test FAILED")
        except ValueError:
            print("invalid GPosT test PASSED")
        assert gpost1.lat() == 0
        assert gpost2.lat() == 1
        assert gpost3.lat() == -90
        passed += 1
        print("latitude test PASSED")
    except AssertionError:
        print("latitude test FAILED")


def test_long():
    global test_total, passed
    test_total += 1
    try:
        assert gpost4.long() == 0
        assert gpost5.long() == 67.54
        assert gpost6.long() == 180
        assert gpost7.long() == -180
        passed += 1
        print("longitude test PASSED")
    except AssertionError:
        print("longitude test FAILED")


def test_west_of():
    global test_total, passed
    test_total += 1
    try:
        assert gpost7.west_of(gpost6)
        assert gpost8.west_of(gpost7) == False
        assert gpost3.west_of(gpost4) == False
        passed += 1
        print("west of test PASSED")
    except AssertionError:
        print("west of test FAILED")


def test_north_of():
    global test_total, passed
    test_total += 1
    try:
        assert gpost1.north_of(gpost2) == False
        assert gpost3.north_of(gpost7) == False
        assert gpost8.north_of(gpost6)
        passed += 1
        print("north of test PASSED")
    except AssertionError:
        print("north of test FAILED")


def test_equal():
    global test_total, passed
    test_total += 1
    try:
        assert gpost11.equal(gpost9)
        assert gpost1.equal(gpost2) == False
        assert gpost5.equal(gpost5)
        assert gpost1.equal(gpost12)
        passed += 1
        print("equal test PASSED")
    except AssertionError:
        print("equal test FAILED")


def test_move():
    global test_total, passed
    test_total += 1
    try:
        gpost1.move(145.435, 35)
        assert gpost1.equal(GPosT(-0.25916667, 0.17861111))
        gpost7.move(34.54, 577)
        assert gpost7.equal(GPosT(84.81083333, -90))
        gpost5.move(-43.523, -43.53)
        assert gpost5.equal(GPosT(-45.71833333, 67.92611111))
        passed += 1
        print("move test PASSED")
    except AssertionError:
        print("move test FAILED")


def test_distance():
    global test_total, passed
    test_total += 1
    try:
        gpost13 = GPosT(2.3, 43.5)
        assert isClose(gpost2.distance(gpost13), 4393)
        assert isClose(gpost3.distance(gpost10), 17260)
        assert isClose(gpost8.distance(gpost12), 10060)
        passed += 1
        print("distance test PASSED")
    except AssertionError:
        print("distance test FAILED")


def test_arrival_date():
    global test_total, passed
    test_total += 1
    try:
        gpost14 = GPosT(34.564, 100.5)
        gpost15 = GPosT(-65.9, -45.5)
        arrival_date = gpost14.arrival_date(gpost15, DateT(1, 1, 2020), 567.65)
        assert arrival_date.equal(DateT(29, 1, 2020))
        arrival_date = gpost3.arrival_date(gpost10, DateT(2, 5, 2018), 1234.54)
        assert arrival_date.equal(DateT(16, 5, 2018))
        arrival_date = gpost2.arrival_date(gpost12, DateT(31, 12, 2004), 600)
        assert arrival_date.equal(DateT(1, 1, 2005))
        arrival_date = gpost8.arrival_date(gpost11, DateT(20, 1, 2020), 10034.33)
        assert arrival_date.equal(DateT(22, 1, 2020))
        passed += 1
        print("arrival date test PASSED")
    except AssertionError:
        print("arrival date test FAILED")


test_lat()
test_long()
test_west_of()
test_north_of()
test_equal()
test_move()
test_distance()
test_arrival_date()

print(passed, "out of", test_total, "tests passed for GPosT")

