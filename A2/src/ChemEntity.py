## @file ChemEntity.py
#  @author Dhruv Bhavsar
#  @brief Abstract interface for methods about chemical entities
#  @date Feb 1, 2020

from abc import ABC, abstractmethod


## @brief
class ChemEntity(ABC):

    ## @brief An abstract method for counting number of atoms
    #  @param element_t
    @abstractmethod
    def num_atoms(self, element_t):
        pass
    
    @abstractmethod
    def constit_elems(self):
        pass
