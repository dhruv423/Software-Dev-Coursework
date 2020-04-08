## @file Equality.py
#  @author Dhruv Bhavsar
#  @brief Used for comparing two objects
#  @Date Feb 1, 2020

from abc import ABC, abstractmethod


## @brief An abstract class for comparing two objects
class Equality(ABC):

    ## @brief Abstract method for checking if two objects are equal
    #  @param other Object to compare against
    #  @return true is equal else false
    @abstractmethod
    def equals(self, other):
        pass
