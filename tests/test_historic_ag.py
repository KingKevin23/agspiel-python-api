#  Copyright (c) 2021 | KingKevin23 (@kingkevin023)

from unittest import TestCase
from datetime import date, datetime
from json import loads

from agspiel.api.historic_ag import HistorischeAg

class TestHistorischeAg(TestCase):
    def setUp(self):
        f = open("testhistoricag.json", "r")
        api_data = loads(f.read())
        f.close()
        self.ag = HistorischeAg(wkn=175353, datum=date(2021, 7, 23), api_data=api_data)

    def test_wkn(self):
        self.assertEqual(self.ag.wkn, 175353)
        self.assertIsInstance(self.ag.wkn, int)

    def test_datum(self):
        self.assertEqual(self.ag.datum, date(2021, 7, 23))
        self.assertIsInstance(self.ag.datum, date)

    def test_name(self):
        self.assertEqual(self.ag.name, "King Kompany")
        self.assertIsInstance(self.ag.name, str)

    def test_gruendung(self):
        self.assertEqual(self.ag.gruendung, datetime(year=2020, month=2, day=4))
        self.assertIsInstance(self.ag.gruendung, datetime)

    def test_aktienanzahl(self):
        self.assertEqual(self.ag.aktienanzahl, 4000000)
        self.assertIsInstance(self.ag.aktienanzahl, int)

#   def test_in_liquidation(self):
#       self.fail()

    def test_kurs(self):
        self.assertEqual(self.ag.kurs, 630)
        self.assertIsInstance(self.ag.kurs, float)

    def test_brief(self):
        self.assertEqual(self.ag.brief, 630)
        self.assertIsInstance(self.ag.brief, float)

    def test_geld(self):
        self.assertEqual(self.ag.geld, 601.99)
        self.assertIsInstance(self.ag.geld, float)

    def test_brief_stueckzahl(self):
        self.assertEqual(self.ag.brief_stueckzahl, 16287)
        self.assertIsInstance(self.ag.brief_stueckzahl, int)

    def test_geld_stueckzahl(self):
        self.assertEqual(self.ag.geld_stueckzahl, 10945)
        self.assertIsInstance(self.ag.geld_stueckzahl, int)

    def test_sw_aktie(self):
        self.assertEqual(self.ag.sw_aktie, 352.26)
        self.assertIsInstance(self.ag.sw_aktie, float)

    def test_bbw_aktie(self):
        self.assertEqual(self.ag.bbw_aktie, 482.78)
        self.assertIsInstance(self.ag.bbw_aktie, float)

    def test_fp_aktie(self):
        self.assertEqual(self.ag.fp_aktie, 436.23)
        self.assertIsInstance(self.ag.fp_aktie, float)

    def test_bw_aktie(self):
        self.assertEqual(self.ag.bw_aktie, 587.09)
        self.assertIsInstance(self.ag.bw_aktie, float)

#   def test_kgv(self):
#       self.fail()

    def test_spread(self):
        self.assertEqual(self.ag.spread, 0.04446031746031742)
        self.assertIsInstance(self.ag.spread, float)

    def test_alter(self):
        self.assertEqual(self.ag.alter, (datetime.now() - self.ag.gruendung).days)
        self.assertIsInstance(self.ag.alter, int)

#   def test_tagesvolumen(self):
#       self.fail()

    def test_boersenwert(self):
        self.assertEqual(self.ag.boersenwert, 2520000000)
        self.assertIsInstance(self.ag.boersenwert, float)

    def test_buchwert(self):
        self.assertEqual(self.ag.buchwert, 2348360222.54)
        self.assertIsInstance(self.ag.buchwert, float)

    def test_depotwert(self):
        self.assertEqual(self.ag.depotwert, 1856199270.98)
        self.assertIsInstance(self.ag.depotwert, float)

    def test_bargeld(self):
        self.assertEqual(self.ag.bargeld, 492160951.56)
        self.assertIsInstance(self.ag.bargeld, float)

    def test_highscore(self):
        self.assertEqual(self.ag.highscore, 49)
        self.assertIsInstance(self.ag.highscore, int)

    def test_highscore_groesse(self):
        self.assertEqual(self.ag.highscore_groesse, 178)
        self.assertIsInstance(self.ag.highscore_groesse, int)

    def test_highscore_wachstum(self):
        self.assertEqual(self.ag.highscore_wachstum, 174)
        self.assertIsInstance(self.ag.highscore_wachstum, int)

#   def test_highscore_newcomer(self):
#       self.fail()

    def test_agsx_punkte(self):
        self.assertEqual(self.ag.agsx_punkte, 1302)
        self.assertIsInstance(self.ag.agsx_punkte, int)

    def test_in_agsx(self):
        self.assertEqual(self.ag.in_agsx, False)
        self.assertIsInstance(self.ag.in_agsx, bool)

    def test_handelsaktivitaet(self):
        self.assertEqual(self.ag.handelsaktivitaet, 94)
        self.assertIsInstance(self.ag.handelsaktivitaet, int)

#   def test_ceo(self):
#       self.fail()
#
#   def test_aktien(self):
#       self.fail()
#
#   def test_anleihen(self):
#       self.fail()
#
#   def test_kredite(self):
#       self.fail()
#
#   def test_zertifikate(self):
#       self.fail()
#
#   def test_orders(self):
#       self.fail()
#
#   def test_aktionaere(self):
#       self.fail()
#
#   def test_kes(self):
#       self.fail()
#
#   def test_khs(self):
#       self.fail()
#
#   def test_dividende(self):
#       self.fail()
#
#   def test_max_zertis(self):
#       self.fail()
#
#   def test_tages_hoch(self):
#       self.fail()
#
#   def test_tages_tief(self):
#       self.fail()
#
#   def test_kurs_14d(self):
#       self.fail()
#
#   def test_kurs_30d(self):
#       self.fail()
#
#   def test_kurs_60d(self):
#       self.fail()
#
#   def test_kurs_90d(self):
#       self.fail()
#
#   def test_bw_14d(self):
#       self.fail()
#
#   def test_bw_30d(self):
#       self.fail()
#
#   def test_bw_60d(self):
#       self.fail()
#
#   def test_bw_90d(self):
#       self.fail()
#
#   def test_fp_14d(self):
#       self.fail()
#
#   def test_fp_30d(self):
#       self.fail()
#
#   def test_fp_60d(self):
#       self.fail()
#
#   def test_fp_90d(self):
#       self.fail()