#!/usr/bin/env python

"""
test_django-laboratory
------------

Tests for `django-laboratory` models module.
"""

from django.test import TestCase
from model_bakery import baker


class TestAuthor(TestCase):
    def setUp(self):
        self.author = baker.make(
            "laboratory.Author",
            given="Sam",
            family="Jennings",
        )

    def test_str(self):
        self.assertEqual(f"{self.author}", self.author.given_family())

    def test_given_family(self):
        self.assertEqual(self.author.given_family(), "Sam Jennings")

    def test_family_given(self):
        self.assertEqual(self.author.family_given(), "Jennings, Sam")

    def test_g_family(self):
        self.assertEqual(self.author.g_family(), "S. Jennings")

    def test_family_g(self):
        self.assertEqual(self.author.family_g(), "Jennings, S.")


class TestLaboratory(TestCase):
    def setUp(self):
        # authors = baker.prepare("laboratory.Author", family="Jennings", _quantity=1)
        self.pub = baker.make(
            "laboratory.Laboratory",
            title=(
                "This should be a really long title so we can test whether the uploaded pdf name is shortened properly"
                " using the simple_file_renamer"
            ),
            CSL={
                "title": (
                    "This should be a really long title so we can test whether the uploaded pdf name is shortened"
                    " properly using the simple_file_renamer"
                )
            },
            # authors=authors,
            # year=2022,
        )

    def test_str(self):
        self.assertEqual(str(self.pub), str(self.pub.citation_key))


class TestCollection(TestCase):
    def setUp(self):
        self.obj = baker.make(
            "laboratory.Collection",
        )

    def test_str(self):
        self.assertEqual(str(self.obj), str(self.obj.name))


# class TestLaboratoryAuthor(TestCase):
#     def setUp(self):
#         lit = baker.make("laboratory.Laboratory")
#         self.obj = baker.make("laboratory.LaboratoryAuthor", laboratory=lit)

#     def test_str(self):
#         self.assertEqual(str(self.obj), str(self.obj.position))
