## @file CompoundT.py
#  @author Dhruv Bhavsar
#  @brief Class for holding a MolecSet
#  @date Feb 3, 2020

from MoleculeT import *
from ChemEntity import *
from Equality import *
from ElmSet import *
from MolecSet import *


## @brief Class that represents a Compound, inherits ChemEntity and Equality
class CompoundT(ChemEntity, Equality):

    ## @brief Constructor to initalize the object with a MolecSet
    #  @param molec_set - MolecSet to be stored in a Compound
    def __init__(self, molec_set):
        self.__C = molec_set

    ## @brief Return the Compound which is a MolecSet
    #  @return MolecSet
    def get_molec_set(self):
        return self.__C

    ## @brief Return the number of atoms in the MolecSet with the specified element
    #  @details Using functional programming functions, turn the
    #           MolecSet into a sequence to iterate over
    #           and find the number of atoms for each MolecSet
    #           with a specified element then sum up the list
    #  @param element - ElementT
    #  @return the total number of atoms of element in the Compound
    def num_atoms(self, element):
        return sum([m.num_atoms(element) for m in self.__C.to_seq()])

    ## @brief Returns the ElmSet of the all the different ElementT in the compound
    #  @details Using get_elm() function for MoleculeT to get the element
    #  @return ElmSet of all the ElementT
    def constit_elems(self):
        return ElmSet([m.get_elm() for m in self.__C.to_seq()])

    ## @brief Check if the two compounds are equal
    #  @param other_compound - other compound to compare with
    #  @return true if equal else false
    def equals(self, other_compound):
        return self.__C.equals(other_compound.get_molec_set())

    def __eq__(self, other):
        return self.equals(other)
