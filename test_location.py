# -*- coding: utf-8 -*-
import sys
import unittest

sys.path.insert(0, '..')

import generate_prep


class TestingPrep(unittest.TestCase):

    def test1(self):
        country = generate_prep.Country("italie")
        preps = ["en ", "l'", "de l'"]
        self.assertListEqual([country.in_prep, country.the_article, country.of_prep], preps)

    def test2(self):
        country = generate_prep.Country("Italie")
        preps = ["en ", "l'", "de l'"]
        self.assertListEqual([country.in_prep, country.the_article, country.of_prep], preps)

    def test3(self):
        country = generate_prep.Country("France")
        preps = ["en ", "la ", "de la "]
        self.assertListEqual([country.in_prep, country.the_article, country.of_prep], preps)

    def test4(self):
        country = generate_prep.Country("japon")
        preps = ["au ", "le ", "du "]
        self.assertListEqual([country.in_prep, country.the_article, country.of_prep], preps)

    def test5(self):
        country = generate_prep.Country("cuba")
        preps = ["à ", "", "de "]
        self.assertListEqual([country.in_prep, country.the_article, country.of_prep], preps)

    def test6(self):
        country = generate_prep.Country("Corée du Sud")
        preps = ["en ", "la ", "de la "]
        self.assertListEqual([country.in_prep, country.the_article, country.of_prep], preps)
