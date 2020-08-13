#  Copyright (c) 2020 | KingKevin23 (@kingkevin023)

from agspiel.api.api import Api
from datetime import datetime
from unittest import TestCase

class TestApi(TestCase):
    def setUp(self):
        self.api = Api("")

    def test_api_version(self):
        self.assertIsInstance(self.api.api_version, int)

    def test_daten_datum(self):
        self.assertIsInstance(self.api.daten_datum, datetime)