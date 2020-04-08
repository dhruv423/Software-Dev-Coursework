## @file Set.py
#  @author Dhruv Bhavsar
#  @brief Class for Set building and applying methods to the Set
#  @date Feb 2, 2020

from Equality import *


## @brief Class that represents a Set
class Set(Equality):

    ## @brief Constructor that initializes the object with set
    #  @details Takes in a sequence and converts it into set and
    #           holds it in the state variable
    #  @param sequence - Takes in a sequence (list)
    def __init__(self, sequence):
        self.__set = set(sequence)

    ## @brief Add an element to the set
    #  @details Uses the add function of set object to add the element
    #  @param Element to add
    def add(self, element):
        self.__set.add(element)

    ## @brief Remove a specified from the set
    #  @details Uses the remove function from the Set Object
    #  @param Specified Element
    #  @throws ValueError if element not in set
    def rm(self, element):
        try:
            self.__set.remove(element)
        except KeyError:
            raise ValueError("Element is not in the set")

    ## @brief Checks if the element is in the set
    #  @param Element to check
    #  @return True if in the set else false
    def member(self, element):
        if element in self.__set:
            return True
        else:
            return False

    ## @brief Returns the size of the set
    #  @details Using len function
    #  @return the size of the set as an integer
    def size(self):
        return len(self.__set)

    ## @brief Checks if the two sets are the same
    #  @details First check if the two sets are the same then
    #           check if all the elements occur in the other set
    #  @param other_set - Set to check with
    #  @return True if the same else false
    def equals(self, other_set):
        if not (self.size() == other_set.size()):
            return False

        for elem in self.__set:
            if not other_set.member(elem):
                return False
        return True

    ## @brief Convert the set into a list for it to be iterable
    #  @return List of the sets
    def to_seq(self):
        return list(self.__set)
