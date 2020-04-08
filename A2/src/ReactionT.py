## @file ReactionT.py
#  @author Dhruv Bhavsar
#  @brief Class that holds two compounds for the reactions
#  @date Feb 3, 2020

from ChemTypes import *
from CompoundT import *
from sympy import Matrix, lcm
import numpy as np


## @brief Class to simulate a reaction with balancing the equation
class ReactionT:

    ## @brief Constructor for ReactionT which balances before storing it
    #  @details Uses local functions to calculate the coeffs, then check
    #           if it is balanced else throw Value Error
    #           The reason I dont check for positive coeffs is
    #           because I make them positive in the calculation of coeffs
    #  @param left_compound - CompoundT right_compound - CompoundT
    def __init__(self, left_compound, right_compound):

        coeffs = self.__calc_coeffs__(left_compound, right_compound)

        left_coeffs = [coeffs[i] for i in range(len(left_compound))]
        right_coeffs = [coeffs[len(left_compound) + i]
                        for i in range(len(right_compound))]

        if not self.__is_balanced__(left_compound, right_compound, left_coeffs, right_coeffs):
            raise ValueError("Not Balanceable")

        self.__rhs = right_compound
        self.__lhs = left_compound
        self.__left_coeffs = left_coeffs
        self.__right_coeffs = right_coeffs

    ## @brief Return the left hand side of ReactionT
    #  @return the left side CompoundT
    def get_lhs(self):
        return self.__lhs

    ## @brief Return the right hand side of ReactionT
    #  @return the right side CompoundT
    def get_rhs(self):
        return self.__rhs

    ## @brief Return the coeffs for the left side
    #  @return list of coeffs
    def get_lhs_coeff(self):
        return self.__left_coeffs

    ## @brief Return the coeffs for the right side
    #  @return list of coeffs
    def get_rhs_coeff(self):
        return self.__right_coeffs

    ## @brief Return the ElementT in the compound
    #  @return ElmSet of elements
    def __elm_in_chem_eq__(self, c):
        new_set = []
        for i in c:
            new_set += i.constit_elems().to_seq()
        return ElmSet(new_set)

    # Function for calculating coefficients,
    # Build the matrix of the rows being the different elements
    # Each index is how many atoms of that element in there
    # The for loop creates each row meaning for a new element
    # The rest of the calculation to find the coefficients using a
    # linear system of equation solver Source:
    # https://stackoverflow.com/questions/42637872/solve-system-of-linear-integer-equations-in-python
    # Throws a Value Error if it can't be solved
    def __calc_coeffs__(self, left_compound, right_compound):
        try:
            left_compound_elms = self.__elm_in_chem_eq__(left_compound).to_seq()
            matrix = []
            for element in left_compound_elms:
                row = \
                    ([m.num_atoms(element)
                      for m in left_compound] + [m.num_atoms(element)
                                                 for m in right_compound])
                matrix.append(row)

            new_matrix = Matrix(matrix)
            v = new_matrix.nullspace()[0]
            m = lcm([val.q for val in v])
            x = m * v
            result = np.array([int(val) for val in x])
            coeffs = list(map(lambda c: abs(c), result))
            return coeffs
        except IndexError:
            raise ValueError("Cannot be balanced")

    # Function to find the number of atoms in a compound for a specified element
    # Also multiply the number of atoms by the coeff
    def __n_atoms__(self, comp, c, element):
        atoms = [c[i] * comp[i].num_atoms(element) for i in range(len(comp))]
        return sum(atoms)

    # Function to find if both the left side and right side have the same
    # number of atoms for a specific element
    def __is_bal_elm__(self, left_comp, right_comp, left_coef, right_coef, element):
        return self.__n_atoms__(left_comp, left_coef, element) \
            == self.__n_atoms__(right_comp, right_coef, element)

    # Function for checking if the reaction has the same elements on the right side
    # and left side. Then checks if the both sides are balanced
    def __is_balanced__(self, left_comp, right_comp, left_coef, right_coef):
        same_elms = \
            self.__elm_in_chem_eq__(left_comp).equals(self.__elm_in_chem_eq__(right_comp))

        balanced_elm = [self.__is_bal_elm__(left_comp, right_comp, left_coef, right_coef, e)
                        for e in self.__elm_in_chem_eq__(left_comp).to_seq()]

        return same_elms and balanced_elm
