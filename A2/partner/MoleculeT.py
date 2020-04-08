## @file ChemTypes.py
#  @author Zihao Du
#  @brief Module that creates the MoleculeT ADT
#  @date Feb 6, 2020

from ChemTypes import *
from ElmSet import *
from ChemEntity import *
from Equality import *


## @brief An abstract data type that represents a Molecule, a child class of
#  ChemEntity and Equality
class MoleculeT(ChemEntity, Equality):

    ## @brief MoleculeT constructor
    #  @details Initializes a MoleculeT object whose state consists
    #  of a natural number and a ElementT object
    #  @param n a natural number(the subscript)
    #  @param e the ElementT object
    def __init__(self, n, e):
        self._num = n
        self._elm = e

    ## @brief Get number of atoms in the molecule
    # @return The number of atoms in the molecule
    def get_num(self):
        return self._num

    ## @brief Get element of the molecule
    # @return The element of the molecule
    def get_elm(self):
        return self._elm

    ## @brief Obtain the number of a certain element in the molecule
    # @return The number of atoms of the element in the molecule
    # @param e ElementT object the client is interested in
    def num_atoms(self, e):
        if (e != self._elm):
            return 0
        else:
            return self._num

    ## @brief Get the element in the molecule in a ElmSet
    # @return ElmSet that contains the element in the molecule
    def constit_elems(self):
        s1 = ElmSet([self._elm])
        return s1

    ## @brief Determine if a molecule is equal to the current molecule
    # @return True if they are the same, otherwise False
    # @param m A moleculeT object to compare with the current one
    def equals(self, m):
        if((m._elm == self._elm) & (m._num == self._num)):
            return True
        else:
            return False
