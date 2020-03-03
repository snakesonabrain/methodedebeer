#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Bruno Stuyts'

# Native Python packages
import unittest
import os

# 3rd party packages
import pandas as pd
import numpy as np

# Project imports
from debeer import calculation


TESTS_DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')


class Test_pilecalcdebeer(unittest.TestCase):

    def setUp(self):
        self.cpt_data = pd.read_excel(os.path.join(TESTS_DATA_DIR, 'debeer_example.xlsx'))

    def test_pilecalcbeer(self):
        calc = calculation.DeBeerCalculation(
            depth=self.cpt_data['z [m]'],
            qc=self.cpt_data['qc [MPa]'],
            diameter_pile=0.4,
            diameter_cone=0.0357)
        calc.resample_data()
        calc.set_soil_layers(
            depth_from=[0, 3, 6, 15],
            depth_to=[3, 6, 15, 20],
            soil_type=['Sand', 'Clay', 'Sand', 'Loam (silt)'])
        calc.calculate_base_resistance()
        calc.correct_shaft_qc(cone_type='U')
        calc.calculate_average_qc()
        calc.calculate_unit_shaft_friction()
        calc.set_shaft_base_factors(
            alpha_b_tertiary_clay=1.0,
            alpha_b_other=1.0,
            alpha_s_tertiary_clay=0.6,
            alpha_s_other=0.6)
        calc.calculate_pile_resistance(
            pile_penetration=16, base_area=0.25*np.pi*(0.4 ** 2), circumference=np.pi * 0.4)
        self.assertAlmostEqual(calc.Rs, 1313.1, 1)
        self.assertAlmostEqual(calc.Rb, 2800.4, 1)
        self.assertAlmostEqual(calc.Rc, 4113.5, 1)