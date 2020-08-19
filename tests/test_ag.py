#  Copyright (c) 2020 | KingKevin23 (@kingkevin023)

import json
from unittest import TestCase
from datetime import datetime
from agspiel.api.ag import Ag
from agspiel.api.data import Data
from agspiel.api.ceo import Ceo
from agspiel.api.aktie import Aktie, Aktionaer
from agspiel.api.anleihe import Anleihe, Kredit
from agspiel.api.zertifikat import Zertifikat
from agspiel.api.order import Order
from bs4 import BeautifulSoup

class TestAg(TestCase):
    def setUp(self):
        f = open("testag.txt", "rb")
        web_data = Data(data=BeautifulSoup(f.read(), "html.parser"), update=lambda: self.data)
        f.close()
        f = open("testapi.txt", "r")
        api_data = Data(data=json.loads(f.read()), update=lambda: self.data)
        f.close()
        self.ag = Ag(wkn=175353, api_data=api_data, web_data=web_data)

    def test_wkn(self):
        self.assertEqual(self.ag.wkn, 175353)
        self.assertIsInstance(self.ag.wkn, int)

    def test_name(self):
        self.assertEqual(self.ag.name, "King Kompany")
        self.assertIsInstance(self.ag.name, str)

    def test_gruendung(self):
        self.assertEqual(self.ag.gruendung, datetime(year=2020, month=2, day=4, hour=16, minute=25, second=5))
        self.assertIsInstance(self.ag.gruendung, datetime)

    def test_aktienanzahl(self):
        self.assertEqual(self.ag.aktienanzahl, 2000000)
        self.assertIsInstance(self.ag.aktienanzahl, int)

    def test_in_liquidation(self):
        self.assertEqual(self.ag.in_liquidation, False)
        self.assertIsInstance(self.ag.in_liquidation, bool)

    def test_kurs(self):
        self.assertEqual(self.ag.kurs, 262)
        self.assertIsInstance(self.ag.kurs, float)

    def test_brief(self):
        self.assertEqual(self.ag.brief, 262)
        self.assertIsInstance(self.ag.brief, float)

    def test_geld(self):
        self.assertEqual(self.ag.geld, 212.8)
        self.assertIsInstance(self.ag.geld, float)

    def test_brief_stueckzahl(self):
        self.assertEqual(self.ag.brief_stueckzahl, 30499)
        self.assertIsInstance(self.ag.brief_stueckzahl, int)

    def test_geld_stueckzahl(self):
        self.assertEqual(self.ag.geld_stueckzahl, 281)
        self.assertIsInstance(self.ag.geld_stueckzahl, int)

    def test_sw_aktie(self):
        self.assertEqual(self.ag.sw_aktie, 52.30)
        self.assertIsInstance(self.ag.sw_aktie, float)

    def test_bbw_aktie(self):
        self.assertEqual(self.ag.bbw_aktie, 59.01)
        self.assertIsInstance(self.ag.bbw_aktie, float)

    def test_fp_aktie(self):
        self.assertEqual(self.ag.fp_aktie, 56.14)
        self.assertIsInstance(self.ag.fp_aktie, float)

    def test_bw_aktie(self):
        self.assertEqual(self.ag.bw_aktie, 107.65)
        self.assertIsInstance(self.ag.bw_aktie, float)

    def test_kgv(self):
        self.assertEqual(self.ag.kgv, 115.59)
        self.assertIsInstance(self.ag.kgv, float)

    def test_spread(self):
        self.assertEqual(self.ag.spread, 0.1877862595419847)
        self.assertIsInstance(self.ag.spread, float)

    def test_alter(self):
        self.assertEqual(self.ag.alter, (datetime.now() - self.ag.gruendung).days)
        self.assertIsInstance(self.ag.alter, int)

    def test_tagesvolumen(self):
        self.assertEqual(self.ag.tagesvolumen, 0)
        self.assertIsInstance(self.ag.tagesvolumen, float)

    def test_boersenwert(self):
        self.assertEqual(self.ag.boersenwert, 524000000)
        self.assertIsInstance(self.ag.boersenwert, float)

    def test_buchwert(self):
        self.assertEqual(self.ag.buchwert, 215306536.68)
        self.assertIsInstance(self.ag.buchwert, float)

    def test_depotwert(self):
        self.assertEqual(self.ag.depotwert, 163698677.84)
        self.assertIsInstance(self.ag.depotwert, float)

    def test_bargeld(self):
        self.assertEqual(self.ag.bargeld, 51607858.84)
        self.assertIsInstance(self.ag.bargeld, float)

    def test_highscore(self):
        self.assertEqual(self.ag.highscore, 381)
        self.assertIsInstance(self.ag.highscore, int)

    def test_highscore_groesse(self):
        self.assertEqual(self.ag.highscore_groesse, 329)
        self.assertIsInstance(self.ag.highscore_groesse, int)

    def test_highscore_wachstum(self):
        self.assertEqual(self.ag.highscore_wachstum, 366)
        self.assertIsInstance(self.ag.highscore_wachstum, int)

    def test_highscore_newcomer(self):
        self.assertEqual(self.ag.highscore_newcomer, 0)
        self.assertIsInstance(self.ag.highscore_newcomer, int)

    def test_agsx_punkte(self):
        self.assertEqual(self.ag.agsx_punkte, 1224)
        self.assertIsInstance(self.ag.agsx_punkte, int)

    def test_in_agsx(self):
        self.assertEqual(self.ag.in_agsx, False)
        self.assertIsInstance(self.ag.in_agsx, bool)

    def test_handelsaktivitaet(self):
        self.assertEqual(self.ag.handelsaktivitaet, 46)
        self.assertIsInstance(self.ag.handelsaktivitaet, int)

    def test_ceo(self):
        self.assertIsInstance(self.ag.ceo, Ceo)
        self.assertEqual(self.ag.ceo.name, "KingKevin23")
        self.assertIsInstance(self.ag.ceo.name, str)
        self.assertEqual(self.ag.ceo.index, "Freibeuter")
        self.assertIsInstance(self.ag.ceo.index, str)
        self.assertEqual(self.ag.ceo.registrierung_datum, datetime(year=2020, month=2, day=4, hour=16, minute=24))
        self.assertIsInstance(self.ag.ceo.registrierung_datum, datetime)
        self.assertEqual(self.ag.ceo.gesperrt, False)
        self.assertIsInstance(self.ag.ceo.gesperrt, bool)
        self.assertEqual(self.ag.ceo.userprojekt, False)
        self.assertIsInstance(self.ag.ceo.userprojekt, bool)

    def test_aktien(self):
        for i in self.ag.aktien:
            self.assertIsInstance(i, Aktie)
        self.assertEqual(self.ag.aktien[0].wkn, 104531)
        self.assertIsInstance(self.ag.aktien[0].wkn, int)
        self.assertEqual(self.ag.aktien[0].stueckzahl, 146)
        self.assertIsInstance(self.ag.aktien[0].stueckzahl, int)
        self.assertEqual(self.ag.aktien[1].wkn, 105516)
        self.assertIsInstance(self.ag.aktien[1].wkn, int)
        self.assertEqual(self.ag.aktien[1].stueckzahl, 23)
        self.assertIsInstance(self.ag.aktien[1].stueckzahl, int)

    def test_anleihen(self):
        for i in self.ag.anleihen:
            self.assertIsInstance(i, Anleihe)
        self.assertEqual(self.ag.anleihen[0].betrag, 10000000)
        self.assertIsInstance(self.ag.anleihen[0].betrag, int)
        self.assertEqual(self.ag.anleihen[0].zins, 0.34)
        self.assertIsInstance(self.ag.anleihen[0].zins, float)
        self.assertEqual(self.ag.anleihen[0].auszahlung_datum, datetime(year=2020, month=8, day=19, hour=15, minute=34, second=14))
        self.assertIsInstance(self.ag.anleihen[0].auszahlung_datum, datetime)
        self.assertEqual(self.ag.anleihen[0].laufzeit, 5)
        self.assertIsInstance(self.ag.anleihen[0].laufzeit, int)

    def test_kredite(self):
        for i in self.ag.kredite:
            self.assertIsInstance(i, Kredit)
        self.assertEqual(self.ag.kredite[0].betrag, 10000000)
        self.assertIsInstance(self.ag.kredite[0].betrag, int)
        self.assertEqual(self.ag.kredite[0].zins, 0.32)
        self.assertIsInstance(self.ag.kredite[0].zins, float)
        self.assertEqual(self.ag.kredite[0].rueckzahlung_datum, datetime(year=2020, month=8, day=14, hour=15, minute=1, second=33))
        self.assertIsInstance(self.ag.kredite[0].rueckzahlung_datum, datetime)
        self.assertEqual(self.ag.kredite[0].laufzeit, 5)
        self.assertIsInstance(self.ag.kredite[0].laufzeit, int)

    def test_zertifikate(self):
        for i in self.ag.zertifikate:
            self.assertIsInstance(i, Zertifikat)
        self.assertEqual(self.ag.zertifikate[0].betrag, 234.43)
        self.assertIsInstance(self.ag.zertifikate[0].betrag, float)
        self.assertEqual(self.ag.zertifikate[0].typ, "call")
        self.assertIsInstance(self.ag.zertifikate[0].typ, str)
        self.assertEqual(self.ag.zertifikate[0].hebel, 1.092)
        self.assertIsInstance(self.ag.zertifikate[0].hebel, float)
        self.assertEqual(self.ag.zertifikate[0].punkte, 23443)
        self.assertIsInstance(self.ag.zertifikate[0].punkte, int)
        self.assertEqual(self.ag.zertifikate[0].ablaufdatum, datetime(year=2020, month=8, day=10, hour=17, minute=48, second=1))
        self.assertIsInstance(self.ag.zertifikate[0].ablaufdatum, datetime)

    def test_orders(self):
        for i in self.ag.orders:
            self.assertIsInstance(i, Order)
        self.assertEqual(self.ag.orders[0].typ, "sell")
        self.assertIsInstance(self.ag.orders[0].typ, str)
        self.assertEqual(self.ag.orders[0].limit, 410)
        self.assertIsInstance(self.ag.orders[0].limit, float)
        self.assertEqual(self.ag.orders[0].stueckzahl, 303)
        self.assertIsInstance(self.ag.orders[0].stueckzahl, int)
        self.assertEqual(self.ag.orders[0].orderregel, False)
        self.assertIsInstance(self.ag.orders[0].orderregel, bool)
        self.assertEqual(self.ag.orders[0].systembank, False)
        self.assertIsInstance(self.ag.orders[0].systembank, bool)
        self.assertEqual(self.ag.orders[0].datum, datetime(year=2020, month=8, day=16, hour=18, minute=33, second=7))
        self.assertIsInstance(self.ag.orders[0].datum, datetime)

    def test_aktionaere(self):
        temp = self.ag.aktionaere
        for i in temp:
            self.assertIsInstance(i, Aktionaer)
        self.assertEqual(len(temp), 48)
        self.assertEqual(temp[0].wkn, 103279)
        self.assertIsInstance(temp[0].wkn, int)
        self.assertEqual(temp[0].stueckzahl, 121495)
        self.assertIsInstance(temp[0].stueckzahl, int)

    def test_dividende(self):
        self.assertEqual(self.ag.dividende, 0)
        self.assertIsInstance(self.ag.dividende, float)

    def test_max_zertis(self):
        self.assertEqual(self.ag.max_zertis, 5)
        self.assertIsInstance(self.ag.max_zertis, int)

    def test_tages_hoch(self):
        self.assertEqual(self.ag.tages_hoch, 423.35)
        self.assertIsInstance(self.ag.tages_hoch, float)

    def test_tages_tief(self):
        self.assertEqual(self.ag.tages_tief, 338.68)
        self.assertIsInstance(self.ag.tages_tief, float)

    def test_kurs_14d(self):
        self.assertEqual(self.ag.kurs_14d, 38.24)
        self.assertIsInstance(self.ag.kurs_14d, float)

    def test_kurs_30d(self):
        self.assertEqual(self.ag.kurs_30d, -0.39)
        self.assertIsInstance(self.ag.kurs_30d, float)

    def test_kurs_60d(self):
        self.assertEqual(self.ag.kurs_60d, 47.26)
        self.assertIsInstance(self.ag.kurs_60d, float)

    def test_kurs_90d(self):
        self.assertEqual(self.ag.kurs_90d, 35.47)
        self.assertIsInstance(self.ag.kurs_90d, float)

    def test_bw_14d(self):
        self.assertEqual(self.ag.bw_14d, -12.32)
        self.assertIsInstance(self.ag.bw_14d, float)

    def test_bw_30d(self):
        self.assertEqual(self.ag.bw_30d, 4.74)
        self.assertIsInstance(self.ag.bw_30d, float)

    def test_bw_60d(self):
        self.assertEqual(self.ag.bw_60d, 28.03)
        self.assertIsInstance(self.ag.bw_60d, float)

    def test_bw_90d(self):
        self.assertEqual(self.ag.bw_90d, 68.96)
        self.assertIsInstance(self.ag.bw_90d, float)

    def test_fp_14d(self):
        self.assertEqual(self.ag.fp_14d, 3.89)
        self.assertIsInstance(self.ag.fp_14d, float)

    def test_fp_30d(self):
        self.assertEqual(self.ag.fp_30d, 5.51)
        self.assertIsInstance(self.ag.fp_30d, float)

    def test_fp_60d(self):
        self.assertEqual(self.ag.fp_60d, 11.74)
        self.assertIsInstance(self.ag.fp_60d, float)

    def test_fp_90d(self):
        self.assertEqual(self.ag.fp_90d, 16.59)
        self.assertIsInstance(self.ag.fp_90d, float)