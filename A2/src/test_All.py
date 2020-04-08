## @file test_All.py
#  @author Dhruv Bhavsar
#  @brief Test Module using Pytest
#  @date Feb 8, 2020

import collections
from pytest import *
from ChemEntity import *
from ChemTypes import *
import ElmSet
import MolecSet
from Equality import *
from CompoundT import *
from MoleculeT import *
from ReactionT import *
from Set import *


# Set
class TestSet:

    def setup_method(self, method):
        x = [1, 12, 10, 15, 37]
        y = ["a", "b", "d", "r", "t"]
        self.intS = Set(x)
        self.stringS = Set(y)

    def teardown_method(self, method):
        self.intS = None
        self.stringS = None

    def test_int_add(self):
        self.intS.add(178)
        assert self.intS.member(178)

    def test_string_add(self):
        self.stringS.add("good")
        assert self.stringS.member("good")

    def test_int_rm(self):
        self.intS.rm(12)
        assert not self.intS.member(12)

    def test_string_rm(self):
        self.stringS.rm("a")
        assert not self.stringS.member("a")

    def test_int_rm_error(self):
        with raises(ValueError):
            self.intS.rm(2)

    def test_string_rm_error(self):
        with raises(ValueError):
            self.stringS.rm("z")

    def test_int_member(self):
        assert self.intS.member(1)

    def test_string_member(self):
        assert self.stringS.member("t")

    def test_int_size(self):
        assert self.intS.size() == 5

    def test_string_size(self):
        assert self.stringS.size() == 5

    def test_int_equals(self):
        new_set = Set([1, 12, 10, 15, 37])
        assert self.intS.equals(new_set)

    def test_string_equals(self):
        new_set = Set(["a", "b", "d", "r", "t"])
        assert self.stringS.equals(new_set)

    def test_int_not_equals(self):
        assert not self.intS.equals(Set([1, 2, 6, 54, 3]))

    def test_string_not_equals(self):
        assert not self.stringS.equals(Set(["a", "b"]))

    def test_int_to_seq(self):
        assert collections.Counter(
            self.intS.to_seq()) == collections.Counter([1, 12, 10, 15, 37])

    def test_string_to_seq(self):
        assert collections.Counter(
            self.stringS.to_seq()) == collections.Counter(["a", "b", "d", "r", "t"])

    def test_int_to_seq_invalid(self):
        assert not collections.Counter(
            self.intS.to_seq()) == collections.Counter([1, 12, 10, 15, 56, 37])

    def test_string_to_seq_invalid(self):
        assert not collections.Counter(
            self.stringS.to_seq()) == collections.Counter(["a", "b", "d", "r", "t", "tyu"])


# MoleculeT
class TestMoleculeT:

    def setup_method(self, method):
        self.f7 = MoleculeT(7, ElementT.F)
        self.h2 = MoleculeT(2, ElementT.H)
        self.o4 = MoleculeT(4, ElementT.O)

    def teardown_method(self, method):
        self.f7 = None
        self.h2 = None
        self.o4 = None

    def test_get_num(self):
        assert self.f7.get_num() == 7

    def test_get_elm(self):
        assert self.h2.get_elm() == ElementT.H

    def test_num_atoms_oxy(self):
        assert self.o4.num_atoms(self.o4.get_elm()) == 4

    def test_num_atoms_fluorine(self):
        assert self.f7.num_atoms(self.f7.get_elm()) == 7

    def test_constit_elems_hydrogen(self):
        assert self.h2.constit_elems().equals(ElmSet([ElementT.H]))

    def test_constit_elems_oxygen(self):
        assert self.o4.constit_elems().equals(ElmSet([ElementT.O]))

    def test_constit_elems_fluorine(self):
        assert self.f7.constit_elems().equals(ElmSet([ElementT.F]))

    def test_equals_hydrogen(self):
        assert self.h2.equals(self.h2)

    def test_equals_fluorine(self):
        assert self.f7.equals(MoleculeT(7, ElementT.F))

    def test_equals_oxygen(self):
        new_mole = MoleculeT(4, ElementT.O)
        assert self.o4.equals(new_mole)

    def test_not_equals(self):
        assert not self.f7.equals(self.o4)


# CompoundT
class TestCompoundT:

    def setup_method(self):
        self.h2so4 = CompoundT(MolecSet([MoleculeT(1, ElementT.S),
                               MoleculeT(4, ElementT.O), MoleculeT(2, ElementT.H)]))
        self.xef5 = CompoundT(MolecSet([MoleculeT(5, ElementT.F), MoleculeT(1, ElementT.Xe)]))
        self.h2o2 = CompoundT(MolecSet([MoleculeT(2, ElementT.H), MoleculeT(2, ElementT.O)]))

    def teardown_method(self):
        self.h2o2 = None
        self.xef5 = None
        self.h2so4 = None

    def test_get_molec_set_h2so4(self):
        assert self.h2so4.get_molec_set().equals(
            MolecSet([MoleculeT(1, ElementT.S),
                      MoleculeT(4, ElementT.O), MoleculeT(2, ElementT.H)]))

    def test_get_molec_set_h2o2(self):
        assert self.h2o2.get_molec_set().equals(MolecSet([MoleculeT(2, ElementT.H),
                                                MoleculeT(2, ElementT.O)]))

    def test_num_atoms_xef5(self):
        assert self.xef5.num_atoms(ElementT.F) == 5

    def test_num_atoms_xef5_2(self):
        assert self.xef5.num_atoms(ElementT.Xe) == 1

    def test_num_atoms_h2so4(self):
        assert self.h2so4.num_atoms(ElementT.F) == 0

    def test_num_atoms_h2so4_2(self):
        assert self.h2so4.num_atoms(ElementT.S) == 1

    def test_constit_elems_h2o2(self):
        assert self.h2o2.constit_elems().equals(ElmSet([ElementT.H, ElementT.O]))

    def test_constit_elems_h2so4(self):
        assert not self.h2so4.constit_elems().equals(ElmSet([ElementT.H, ElementT.O]))

    def test_constit_elems_xef5(self):
        assert self.xef5.constit_elems().equals(ElmSet([ElementT.Xe, ElementT.F]))

    def test_equals_1(self):
        assert self.xef5.equals(self.xef5)

    def test_equals_2(self):
        molec_set = CompoundT(MolecSet([MoleculeT(1, ElementT.S),
                              MoleculeT(4, ElementT.O), MoleculeT(2, ElementT.H)]))
        assert self.h2so4.equals(molec_set)

    def test_equals_3(self):
        assert not self.h2o2 == self.h2so4


# ReactionT
class TestReactionT:

    def setup_method(self, method):
        self.xe = CompoundT(MolecSet([MoleculeT(1, ElementT.Xe)]))
        self.f2 = CompoundT(MolecSet([MoleculeT(2, ElementT.F)]))
        self.xef6 = CompoundT(MolecSet([MoleculeT(6, ElementT.F), MoleculeT(1, ElementT.Xe)]))

        self.xef6_reaction = ReactionT([self.xe, self.f2], [self.xef6])

        self.h2 = CompoundT(MolecSet([MoleculeT(2, ElementT.H)]))
        self.o2 = CompoundT(MolecSet([MoleculeT(2, ElementT.O)]))
        self.h2o = CompoundT(MolecSet([MoleculeT(2, ElementT.H), MoleculeT(1, ElementT.O)]))

        self.h2o_reaction = ReactionT([self.h2, self.o2], [self.h2o])

        self.c3h8 = CompoundT(MolecSet([MoleculeT(3, ElementT.C), MoleculeT(8, ElementT.H)]))
        self.co2 = CompoundT(MolecSet([MoleculeT(1, ElementT.C), MoleculeT(2, ElementT.O)]))

        self.co2h20_reaction = ReactionT([self.c3h8, self.o2], [self.co2, self.h2o])

    def teardown_method(self, method):
        self.xef5 = None
        self.co2h20 = None
        self.h20 = None

    def test_init_invalid(self):
        with raises(ValueError):
            na = CompoundT(MolecSet([MoleculeT(1, ElementT.Na)]))
            naoh = CompoundT(MolecSet([MoleculeT(1, ElementT.Na), MoleculeT(1, ElementT.H),
                                       MoleculeT(1, ElementT.O)]))
            ReactionT([na, self.h2o], [naoh])

    def test_get_lhs_1(self):
        assert self.h2o_reaction.get_lhs() == [self.h2, self.o2]

    def test_get_lhs_2(self):
        assert self.co2h20_reaction.get_lhs() == [self.c3h8, self.o2]

    def test_get_rhs_1(self):
        assert self.h2o_reaction.get_rhs() == [self.h2o]

    def test_get_rhs_2(self):
        assert self.xef6_reaction.get_rhs() == [self.xef6]

    def test_get_lhs_coeff_1(self):
        assert self.xef6_reaction.get_lhs_coeff() == [1, 3]

    def test_get_lhs_coeff_2(self):
        assert self.co2h20_reaction.get_lhs_coeff() == [1, 5]

    def test_get_lhs_coeff_3(self):
        assert self.h2o_reaction.get_lhs_coeff() == [2, 1]

    def test_get_rhs_coeff_1(self):
        assert self.xef6_reaction.get_rhs_coeff() == [1]

    def test_get_rhs_coeff_2(self):
        assert self.co2h20_reaction.get_rhs_coeff() == [3, 4]

    def test_get_rhs_coeff_3(self):
        assert self.h2o_reaction.get_rhs_coeff() == [2]
