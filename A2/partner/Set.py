## @file Set.py
#  @author Zihao Du
#  @brief Module that creates the Set generic abstract data type
#  @date Feb 6, 2020

from Equality import *


## @brief A generic abstract data type that represents a set
class Set(Equality):

    ## @brief Set constructor
    #  @details Initializes a Set object whose state consists
    #  of a sequence of some type
    #  @param s sequence of some type
    def __init__(self, s):
        self._S = set(s)

    ## @brief Add an element into the Set object
    def add(self, e):
        self._S.add(e)

    ## @brief Remove a certain element in the set
    #  @throw If the element is not in the set, a ValueError will be raised
    # @param e The element the client wants to delete
    def rm(self, e):
        if (self.member(e) is False):
            raise ValueError
        self._S.remove(e)

    ## @brief Determine if a certain element is in the set
    # @return True if the element is in the set, False otherwise
    # @param e The element the client want to test
    def member(self, e):
        for x in self._S:
            if (x == e):
                return True
        return False

    ## @brief Obtain the number of elements in the Set
    # @return The number of elements in the Set
    def size(self):
        return len(self._S)

    ## @brief Inherit from Equality,
    #  determine if a certain Set object equals the current one
    # @return True if they are the same set, False otherwise
    # @param r The Set object to compare with the current Set
    def equals(self, r):
        if (r.size() != self.size()):
            return False
        for e in self._S:
            if (r.member(e) is False):
                return False
        return True

    ## @brief Obtain the list of elements in the set
    # @return List of elements in the set
    def to_seq(self):
        return list(self._S)

    ## @brief Magic function, redefine the meaning of equivalence
    # @return True if two sets are the same set
    # @param r The Set object to compare with the current Set
    def __eq__(self, r):
        if (r.size() != self.size()):
            return False
        for e in self._S:
            if (r.member(e) is False):
                return False
        return True
