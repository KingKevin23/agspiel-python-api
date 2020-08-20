#  Copyright (c) 2020 | KingKevin23 (@kingkevin023)

import json
from unittest import TestCase
from bs4 import BeautifulSoup
from agspiel.api.markt import Markt
from agspiel.api.data import Data

class TestMarkt(TestCase):
    def setUp(self):
        f = open("testmarkt.txt", "rb")
        web_data = Data(data=BeautifulSoup(f.read(), "html.parser"), update=lambda: self.data)
        f.close()
        f = open("testapi.txt", "r")
        api_data = Data(data=json.loads(f.read()), update=lambda: self.data)
        f.close()
        self.markt = Markt(api_data=api_data, web_data=web_data)

    def test_ags(self):
        self.assertEqual(self.markt.ags, 756)
        self.assertIsInstance(self.markt.ags, int)

    def test_orders_24(self):
        self.assertEqual(self.markt.orders_24, 2696)
        self.assertIsInstance(self.markt.orders_24, int)

    def test_volumen_24(self):
        self.assertEqual(self.markt.volumen_24, 762733417.37)
        self.assertIsInstance(self.markt.volumen_24, float)

    def test_agsx_punkte(self):
        self.assertEqual(self.markt.agsx_punkte, 23332)
        self.assertIsInstance(self.markt.agsx_punkte, int)

    def test_agsx_aenderung(self):
        self.assertEqual(self.markt.agsx_aenderung, -42)
        self.assertIsInstance(self.markt.agsx_aenderung, int)

    def test_put_hebel(self):
        self.assertEqual(self.markt.put_hebel, 4.3)
        self.assertIsInstance(self.markt.put_hebel, float)

    def test_call_hebel(self):
        self.assertEqual(self.markt.call_hebel, 1.04)
        self.assertIsInstance(self.markt.call_hebel, float)

    def test_anleihenzins(self):
        self.assertEqual(self.markt.anleihenzins, 1.5)
        self.assertIsInstance(self.markt.anleihenzins, float)