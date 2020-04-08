## @file MoleculeT.py
#  @author Dhruv Bhavsar
#  @brief Class for holding the Molecule which includes element and number of it
#  @date Feb 3, 2020

from ChemTypes import *
from ChemEntity import *
from Equality import *
from ElmSet import *


## @brief Class that represents a molecule, inherits ChemEntity and Equality
class MoleculeT(ChemEntity, Equality):

    ## @brief Constructor that intializes a Molecule with element and number of those element
    #  @param num - number of element in that molecule, elm - ElementT
    def __init__(self, num, elm):
        self.__num = num
        self.__elm = elm

    ## @brief Get the number of atoms in the molecule
    #  @return the number of atoms of the element
    def get_num(self):
        return self.__num

    ## @brief Get the element
    #  @return ElementT of element
    def get_elm(self):
        return self.__elm

    ## @brief Return the number of atom in the Molecule
    #  @details If the inputted element if the same as the MoleculeT
    #           then return the number of atoms else 0
    #  @param element - ElementT to get
    #  @return Number of atoms or 0
    def num_atoms(self, element):
        if self.__elm == element:
            return self.__num
        else:
            return 0

    ## @brief Return the element in a ElmSet
    #  @return ElmSet of the element
    def constit_elems(self):
        return ElmSet([self.__elm])

    ## @brief Check if the other MoleculeT is the same as current object
    #  @details Checking by if it is the same ElementT and same number of atoms
    #  @param other_m - MoleculeT to compare with
    #  @return True if the same else False
    def equals(self, other_m):
        return self.__elm == other_m.__elm and self.__num == other_m.__num

    ## @brief The default equals for Python
    #  @details But we don't want that we want to use our equals method
    #  @param Other - MoleculeT
    #  @return the result of our equals method
    def __eq__(self, other):
        return self.equals(other)

    def __hash__(self):
        return hash(str(self.__elm) + str(self.__num))
