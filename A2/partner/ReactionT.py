## @file ReactionT.py
#  @author Zihao Du
#  @brief Module that creates the ReactionT ADT
#  @date Feb 6, 2020

from ChemTypes import *
from CompoundT import *
from numpy import *


## @brief An abstract data type that represents a chemical reaction
class ReactionT:

    ## @brief ReactionT constructor
    #  @details Initializes a ReactionT object whose state consists
    #  of two sequences of CompoundT, two sequences of real numbers.
    #  The constructor will calculate the two sequences of coefficients using
    #  linear system of equations solver.
    #  @throw If any coefficient is zero or negative,
    #  or the number of compounds is not number of elements plus one,
    #  or the reaction cannot be balanced, a ValueError will be raised.
    #  @param l sequence of CompoundT representing the left hand side of the reaction
    #  @param r sequence of CompoundT representing the right hand side of the reaction
    def __init__(self, l, r):
        if (__elm_in_chem_eq__(l) != __elm_in_chem_eq__(r)):
            raise ValueError
        elements = __elm_in_chem_eq__(l)
        a = []
        b = []
        for elm in elements.to_seq():
            b.append([-(l[0].num_atoms(elm))])
            row = []
            for m in (l + r)[1:]:
                row.append(m.num_atoms(elm))
            a.append(row)
        if (len(a) != len(a[0])):
            raise ValueError
        coeff = linalg.solve(a, b)
        lhsc = [1]
        rhsc = []
        for i in range(len(l) - 1):
            lhsc.append(float(coeff[i][0]))
        for i in range(len(r)):
            rhsc.append(float(coeff[len(l) - 1 + i][0]))
        rhsc = [-x for x in rhsc]
        if(__is_balanced__(l, r, lhsc, rhsc) is False):
            raise ValueError
        if (__pos__(rhsc) is False or __pos__(lhsc) is False):
            raise ValueError
        self._lhs = l
        self._rhs = r
        self._coeffl = lhsc
        self._coeffr = rhsc

    ## @brief Obtain the sequence of CompoundT representing the left hand side
    # @return The sequence of CompoundT representing the left hand side
    def get_lhs(self):
        return self._lhs

    ## @brief Obtain the sequence of CompoundT representing the right hand side
    # @return The sequence of CompoundT representing the right hand side
    def get_rhs(self):
        return self._rhs

    ## @brief Obtain the list of real numbers representing the left hand side coefficients
    # @return The sequence of real numbers representing the left hand side coefficients
    def get_lhs_coeff(self):
        return self._coeffl

    ## @brief Obtain the list of real numbers representing the right hand side coefficients
    # @return The sequence of real numbers representing the right hand side coefficients
    def get_rhs_coeff(self):
        return self._coeffr


## @brief Determine if a sequence of real numbers have a positive or zero element in it
#  @param s List of real numbers
#  @return True if all elements are positive, otherwise False
def __pos__(s):
    for m in s:
        if (m <= 0):
            return False
    return True


## @brief Count the number of a certain atom on one side of the reaction
#  @param cs List of CompoundT
#  @param c List of coefficients
#  @param e A certain Element the client wants to count
#  @return The number of atoms of a certain element in one side of the reaction
def __n_atoms__(cs, c, e):
    sum = 0
    for i in range(len(cs)):
        sum += (c[i] * cs[i].num_atoms(e))
    return sum


## @brief List all the elements that appear in a sequence of CompoundT
#  @param C List of CompoundT
#  @return A ElmSet of elements that appears in the sequence of compounds
def __elm_in_chem_eq__(c):
    s = ElmSet([])
    for com in c:
        for e in (com.constit_elems().to_seq()):
            s.add(e)
    return s


## @brief Determine if two sides of a reaction achieve a balance in a certain element
#  @param l List of CompoundT on one side
#  @param r List of CompoundT on the other side
#  @param cl List of coefficients on one side
#  @param cl List of coefficients on the other side
#  @param e A certain Element the client wants to count
#  @return True if the number of atoms of the element is equal, otherwise False
def __is_bal_elm__(l, r, cl, cr, e):
    return (__n_atoms__(l, cl, e) == __n_atoms__(r, cr, e))


## @brief Determine if two sides of a reaction is balanced
#  @param l List of CompoundT on one side
#  @param r List of CompoundT on the other side
#  @param cl List of coefficients on one side
#  @param cl List of coefficients on the other side
#  @return True if they achieve a balance, otherwise False
def __is_balanced__(l, r, cl, cr):
    for e in (__elm_in_chem_eq__(l)).to_seq():
        if (__is_bal_elm__(l, r, cl, cr, e) is False):
            return False
    if (__elm_in_chem_eq__(l) != __elm_in_chem_eq__(r)):
        return False
    return True
