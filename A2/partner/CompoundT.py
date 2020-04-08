## @file CompoundT.py
#  @author Zihao Du
#  @brief Module that creates the CompoundT ADT
#  @date Feb 6, 2020

from MoleculeT import *
from MolecSet import *
from ElmSet import *
from ChemEntity import *
from Equality import *


## @brief An abstract data type that represents a compound(set of molecules), a
#  child class of ChemEntity and Equality
class CompoundT(ChemEntity, Equality):

    ## @brief CompoundT constructor
    #  @details Initializes a CompoundT object whose state consists
    #  of a MolecSet
    #  @param m A MolecSet
    def __init__(self, m):
        self._C = m

    ## @brief Obtain the MolecSet of the compound
    # @return The MolecSet of the compound
    def get_molec_set(self):
        return self._C

    ## @brief Inherit from ChemEntity,
    #  obtain the number of atoms of a certain element in the compound
    # @return The number of atoms of a certain element in the compound
    # @param e ElementT object the client is interested in
    def num_atoms(self, e):
        sum = 0
        for m in (self._C).to_seq():
            sum += m.num_atoms(e)
        return sum

    ## @brief Inherit from ChemEntity,
    #  obtain the set of Elements in the compound
    # @return An ElmSet containing all elements that appears in the compound
    def constit_elems(self):
        set1 = ElmSet([])
        for m in (self._C).to_seq():
            set1.add(m.get_elm())
        return set1

    ## @brief Inherit from Equality,
    #  determine if two compounds are the same
    # @return True if two compounds have the same molecules inside
    # @param d CompoundT object to compare with the current one
    def equals(self, d):
        return (self._C.equals(d.get_molec_set()))

    ## @brief Magic method, determine if two compounds are the same
    # @return True if two compounds have the same molecules inside
    # @param d CompoundT object to compare with the current one
    def __eq__(self, d):
        return (self._C.equals(d.get_molec_set()))
