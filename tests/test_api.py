#  Copyright (c) 2020 | KingKevin23 (@kingkevin023)

from agspiel.api import Api
from unittest import TestCase

class TestApi(TestCase):
    def test_get_ag(self):
        api = Api("")
        api.get_ag(100001)
