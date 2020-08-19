#  Copyright (c) 2020 | KingKevin23 (@kingkevin023)

import re
from bs4 import BeautifulSoup
from datetime import datetime
from .ceo import Ceo
from .aktie import Aktie, Aktionaer
from .anleihe import Anleihe, Kredit
from .zertifikat import Zertifikat
from .order import Order
from .data import Data

class Ag:
    def __init__(self, wkn:int, api_data:Data, web_data:Data):
        self._wkn:int = wkn
        self._api_data:Data = api_data
        self._web_data:Data = web_data
        self._ag_data = lambda: self._api_data().get("ags").get(str(self.wkn))

    @property
    def wkn(self) -> int:
        return self._wkn

    @property
    def name(self) -> str:
        return self._ag_data().get("name")

    @property
    def gruendung(self) -> datetime:
        return datetime.strptime(self._ag_data().get("gruendung"), "%Y-%m-%d %H:%M:%S")

    @property
    def aktienanzahl(self) -> int:
        return int(self._ag_data().get("aktienanzahl"))

    @property
    def in_liquidation(self) -> bool:
        return self._ag_data().get("in_liquidation") == "true"

    @property
    def kurs(self) -> float:
        return float(self._ag_data().get("kurs"))

    @property
    def brief(self) -> float:
        return float(self._ag_data().get("brief"))

    @property
    def geld(self) -> float:
        return float(self._ag_data().get("geld"))

    @property
    def brief_stueckzahl(self) -> int:
        return int(self._ag_data().get("brief_stueckzahl"))

    @property
    def geld_stueckzahl(self) -> int:
        return int(self._ag_data().get("geld_stueckzahl"))

    @property
    def sw_aktie(self) -> float:
        return float(re.compile("-?\d*[.]?\d*[,]\d{2}").findall(self._web_data().find("div", attrs={"id":"sw"}).text)[0]
                            .replace(".", "").replace(",", "."))

    @property
    def bbw_aktie(self) -> float:
        return float(re.compile("-?\d*[.]?\d*[,]\d{2}").findall(self._web_data().find("div", attrs={"id": "bbw"}).text)[0]
                             .replace(".", "").replace(",", "."))

    @property
    def fp_aktie(self) -> float:
        return float(re.compile("-?\d*[.]?\d*[,]\d{2}").findall(self._web_data().find("div", attrs={"id": "fp"}).text)[0]
                            .replace(".", "").replace(",", "."))

    @property
    def bw_aktie(self) -> float:
        return round(self.buchwert / self.aktienanzahl, 2)

    @property
    def kgv(self) -> float:
        return float(re.compile("\d*[,]\d*").findall(self._web_data().find("div", attrs={"id":"kgv"}).text)[0].
                       replace(",", "."))

    @property
    def spread(self) -> float:
        if self.geld == 0 or self.brief == 0:
            return 0
        else:
            return 1 - (self.geld / self.brief)

    @property
    def alter(self) -> int:
        return (datetime.now() - self.gruendung).days

    @property
    def tagesvolumen(self) -> float:
        return Ag._convert_number(self._web_data().find("div", attrs={"id":"tagesvolumen"}).text)

    @property
    def boersenwert(self) -> float:
        return self.kurs * self.aktienanzahl

    @property
    def buchwert(self) -> float:
        return self.depotwert + self.bargeld

    @property
    def depotwert(self) -> float:
        return float(self._ag_data().get("depotwert"))

    @property
    def bargeld(self) -> float:
        return float(self._ag_data().get("bargeld"))

    @property
    def highscore(self) -> int:
        return int(self._ag_data().get("highscore_platz"))

    @property
    def highscore_groesse(self) -> int:
        return int(self._ag_data().get("highscore_platz_groesse"))

    @property
    def highscore_wachstum(self) -> int:
        return int(self._ag_data().get("highscore_platz_wachstum"))

    @property
    def highscore_newcomer(self) -> int:
        return int(self._ag_data().get("highscore_platz_newcomer"))

    @property
    def agsx_punkte(self) -> int:
        return int(self._ag_data().get("agsx_punkte"))

    @property
    def in_agsx(self) -> bool:
        return self._ag_data().get("in_agsx") == "true"

    @property
    def handelsaktivitaet(self) -> int:
        return int(self._ag_data().get("handelsaktivitaet"))

    @property
    def ceo(self) -> Ceo:
        name = self._ag_data().get("ceo").get("name")
        try:
            index = re.compile("Spielerindex:.(.*)").findall(self._web_data().find("img", attrs={"width": "150"})
                                                             .attrs.get("title"))[0]
        except AttributeError:  # Für den Fall das Spieler in keinem Index ist
            index = None
        registrierung_datum = datetime.strptime(self._ag_data().get("ceo").get("registrierung_datum"), "%Y-%m-%d %H:%M:%S")
        gesperrt = self._ag_data().get("ceo").get("gesperrt") == "true"
        userprojekt = self._ag_data().get("ceo").get("ist_userprojekt_account") == "true"
        return Ceo(name=name, index=index, registrierung_datum=registrierung_datum, gesperrt=gesperrt, 
                   userprojekt=userprojekt)

    @property
    def aktien(self) -> list:
        aktien = []
        for i in self._ag_data().get("aktien"):
            temp = Aktie(wkn=int(i.get("wkn")), stueckzahl=int(i.get("stueckzahl")))
            aktien.append(temp)

        return aktien

    @property
    def anleihen(self) -> list:
        anleihen = []
        for i in self._ag_data().get("anleihen"):
            temp = Anleihe(betrag=int(i.get("betrag")), zins=float(i.get("zins")),
                           auszahlung_datum=datetime.strptime(i.get("auszahlung_datum"), "%Y-%m-%d %H:%M:%S"),
                           laufzeit=int(i.get("laufzeit")))
            anleihen.append(temp)

        return anleihen

    @property
    def kredite(self) -> list:
        kredite = []
        for i in self._ag_data().get("kredite"):
            temp = Kredit(betrag=int(i.get("betrag")), zins=float(i.get("zins")),
                          rueckzahlung_datum=datetime.strptime(i.get("rueckzahlung_datum"), "%Y-%m-%d %H:%M:%S"),
                          laufzeit=int(i.get("laufzeit")))
            kredite.append(temp)

        return kredite

    @property
    def zertifikate(self) -> list:
        zertifikate = []
        for i in self._ag_data().get("zertifikate"):
            try:
                hebel = float(i.get("hebel"))
            except TypeError: # falls hebel noch nicht bekannt
                hebel = 0
            typ = i.get("typ")
            temp = Zertifikat(betrag=float(i.get("betrag")), typ=typ, hebel=hebel, punkte=int(i.get("punkte")),
                              ablaufdatum=datetime.strptime(i.get("ablauf_datum"), "%Y-%m-%d %H:%M:%S"))
            zertifikate.append(temp)

        return zertifikate

    @property
    def orders(self) -> list:
        orders = []
        for i in self._ag_data().get("orders"):
            temp = Order(typ=i.get("typ"), limit=float(i.get("limit")), stueckzahl=int(i.get("stueckzahl")),
                         orderregel=i.get("orderregel") == "true", systembank=i.get("systembank_order") == "true",
                         datum=datetime.strptime(i.get("datum"), "%Y-%m-%d %H:%M:%S"))
            orders.append(temp)

        return orders

    @property
    def aktionaere(self) -> list:
        aktionaere = []
        for ag in self._api_data().get("ags").values():
            for aktie in ag.get("aktien"):
                if self.wkn in aktie.values():
                    aktionaere.append(Aktionaer(wkn=ag.get("wkn"), stueckzahl=aktie.get("stueckzahl")))

        return aktionaere

    @property
    def dividende(self) -> float:
        table_data = {}
        rows = self._web_data().find('table', attrs={'class': 'padding5'}).find_all('tr')
        for row in rows:
            cols = row.find_all("td")
            table_data[cols[0].text] = cols[1].text

        return float(re.compile("(0\.?\d{0,2})%").findall(table_data.get("Dividende"))[0])

    @property
    def max_zertis(self) -> int:
        table_data = {}
        rows = self._web_data().find('table', attrs={'class': 'padding5'}).find_all('tr')
        for row in rows:
            cols = row.find_all("td")
            table_data[cols[0].text] = cols[1].text

        return int(re.compile("(\d{1,2})%").findall(table_data.get("Max. Zertifikatevol."))[0])

    @property
    def tages_hoch(self) -> float:
        table_data = {}
        rows = self._web_data().find('table', attrs={'class': 'padding5'}).find_all('tr')
        for row in rows:
            cols = row.find_all("td")
            table_data[cols[0].text] = cols[1].text

        return float(re.compile("\d*\.?\d*,?\d*").findall(table_data.get("Tageshoch"))[0].replace(".", "").
                              replace(",", "."))

    @property
    def tages_tief(self) -> float:
        table_data = {}
        rows = self._web_data().find('table', attrs={'class': 'padding5'}).find_all('tr')
        for row in rows:
            cols = row.find_all("td")
            table_data[cols[0].text] = cols[1].text

        return float(re.compile("\d*\.?\d*,?\d*").findall(table_data.get("Tagestief"))[0].replace(".", "").
                              replace(",", "."))

    @property
    def kurs_14d(self) -> float:
        table_data = []
        rows = self._web_data().find('table', attrs={'class': 'normalborder'}).find_all('tr')
        for row in rows:
            cols = row.find_all("td")
            for col in cols:
                inhalt = col.find_all("span")
                try:
                    table_data.append(float(inhalt[0].text.replace(".", "").replace(",", ".")))
                except IndexError:
                    pass

        offset = int(len(table_data) / 3) - 1
        if len(table_data) >= 3:
            kurs_14d = table_data[0]
        else:
            kurs_14d = None

        return kurs_14d

    @property
    def kurs_30d(self) -> float:
        table_data = []
        rows = self._web_data().find('table', attrs={'class': 'normalborder'}).find_all('tr')
        for row in rows:
            cols = row.find_all("td")
            for col in cols:
                inhalt = col.find_all("span")
                try:
                    table_data.append(float(inhalt[0].text.replace(".", "").replace(",", ".")))
                except IndexError:
                    pass

        offset = int(len(table_data) / 3) - 1
        if len(table_data) >= 6:
            kurs_30d = table_data[1]
        else:
            kurs_30d = None

        return kurs_30d

    @property
    def kurs_60d(self) -> float:
        table_data = []
        rows = self._web_data().find('table', attrs={'class': 'normalborder'}).find_all('tr')
        for row in rows:
            cols = row.find_all("td")
            for col in cols:
                inhalt = col.find_all("span")
                try:
                    table_data.append(float(inhalt[0].text.replace(".", "").replace(",", ".")))
                except IndexError:
                    pass

        offset = int(len(table_data) / 3) - 1
        if len(table_data) >= 9:
            kurs_60d = table_data[2]
        else:
            kurs_60d = None

        return kurs_60d

    @property
    def kurs_90d(self) -> float:
        table_data = []
        rows = self._web_data().find('table', attrs={'class': 'normalborder'}).find_all('tr')
        for row in rows:
            cols = row.find_all("td")
            for col in cols:
                inhalt = col.find_all("span")
                try:
                    table_data.append(float(inhalt[0].text.replace(".", "").replace(",", ".")))
                except IndexError:
                    pass

        offset = int(len(table_data) / 3) - 1
        if len(table_data) >= 12:
            kurs_90d = table_data[3]
        else:
            kurs_90d = None

        return kurs_90d

    @property
    def bw_14d(self) -> float:
        table_data = []
        rows = self._web_data().find('table', attrs={'class': 'normalborder'}).find_all('tr')
        for row in rows:
            cols = row.find_all("td")
            for col in cols:
                inhalt = col.find_all("span")
                try:
                    table_data.append(float(inhalt[0].text.replace(".", "").replace(",", ".")))
                except IndexError:
                    pass

        offset = int(len(table_data) / 3) - 1
        if len(table_data) >= 3:
            bw_14d = table_data[1 + offset]
        else:
            bw_14d = None

        return bw_14d

    @property
    def bw_30d(self) -> float:
        table_data = []
        rows = self._web_data().find('table', attrs={'class': 'normalborder'}).find_all('tr')
        for row in rows:
            cols = row.find_all("td")
            for col in cols:
                inhalt = col.find_all("span")
                try:
                    table_data.append(float(inhalt[0].text.replace(".", "").replace(",", ".")))
                except IndexError:
                    pass

        offset = int(len(table_data) / 3) - 1
        if len(table_data) >= 6:
            bw_30d = table_data[2 + offset]
        else:
            bw_30d = None

        return bw_30d

    @property
    def bw_60d(self) -> float:
        table_data = []
        rows = self._web_data().find('table', attrs={'class': 'normalborder'}).find_all('tr')
        for row in rows:
            cols = row.find_all("td")
            for col in cols:
                inhalt = col.find_all("span")
                try:
                    table_data.append(float(inhalt[0].text.replace(".", "").replace(",", ".")))
                except IndexError:
                    pass

        offset = int(len(table_data) / 3) - 1
        if len(table_data) >= 9:
            bw_60d = table_data[3 + offset]
        else:
            bw_60d = None

        return bw_60d

    @property
    def bw_90d(self) -> float:
        table_data = []
        rows = self._web_data().find('table', attrs={'class': 'normalborder'}).find_all('tr')
        for row in rows:
            cols = row.find_all("td")
            for col in cols:
                inhalt = col.find_all("span")
                try:
                    table_data.append(float(inhalt[0].text.replace(".", "").replace(",", ".")))
                except IndexError:
                    pass

        offset = int(len(table_data) / 3) - 1
        if len(table_data) >= 12:
            bw_90d = table_data[4 + offset]
        else:
            bw_90d = None

        return bw_90d

    @property
    def fp_14d(self) -> float:
        table_data = []
        rows = self._web_data().find('table', attrs={'class': 'normalborder'}).find_all('tr')
        for row in rows:
            cols = row.find_all("td")
            for col in cols:
                inhalt = col.find_all("span")
                try:
                    table_data.append(float(inhalt[0].text.replace(".", "").replace(",", ".")))
                except IndexError:
                    pass

        offset = int(len(table_data) / 3) - 1
        if len(table_data) >= 3:
            fp_14d = table_data[2 + offset * 2]
        else:
            fp_14d = None

        return fp_14d

    @property
    def fp_30d(self) -> float:
        table_data = []
        rows = self._web_data().find('table', attrs={'class': 'normalborder'}).find_all('tr')
        for row in rows:
            cols = row.find_all("td")
            for col in cols:
                inhalt = col.find_all("span")
                try:
                    table_data.append(float(inhalt[0].text.replace(".", "").replace(",", ".")))
                except IndexError:
                    pass

        offset = int(len(table_data) / 3) - 1
        if len(table_data) >= 6:
            fp_30d = table_data[3 + offset * 2]
        else:
            fp_30d = None

        return fp_30d

    @property
    def fp_60d(self) -> float:
        table_data = []
        rows = self._web_data().find('table', attrs={'class': 'normalborder'}).find_all('tr')
        for row in rows:
            cols = row.find_all("td")
            for col in cols:
                inhalt = col.find_all("span")
                try:
                    table_data.append(float(inhalt[0].text.replace(".", "").replace(",", ".")))
                except IndexError:
                    pass

        offset = int(len(table_data) / 3) - 1
        if len(table_data) >= 9:
            fp_60d = table_data[4 + offset * 2]
        else:
            fp_60d = None

        return fp_60d

    @property
    def fp_90d(self) -> float:
        table_data = []
        rows = self._web_data().find('table', attrs={'class': 'normalborder'}).find_all('tr')
        for row in rows:
            cols = row.find_all("td")
            for col in cols:
                inhalt = col.find_all("span")
                try:
                    table_data.append(float(inhalt[0].text.replace(".", "").replace(",", ".")))
                except IndexError:
                    pass

        offset = int(len(table_data) / 3) - 1
        if len(table_data) >= 12:
            fp_90d = table_data[5 + offset * 2]
        else:
            fp_90d = None

        return fp_90d

    @staticmethod
    def _convert_number(number: str) -> float:
        """
        Diese Methode wandelt Zahlen in der Form "5,6 Mio." in Gleitkommazahlen um.

        :param number: Die umzuwandelnde Zahl
        :return: Die umgewandelte Gleitkommazahl
        """
        ergebnis = float(re.compile("\d+[,]?\d*").findall(number)[0].replace(",", "."))
        multiplier = re.compile("\d*[,]?\d*.(:Mrd\.|Mio\.|Tsd\.)").findall(number)
        if multiplier:
            multiplier = multiplier[0]
            if multiplier == "Mrd.":
                ergebnis *= 1000000000
            elif multiplier == "Mio.":
                ergebnis *= 1000000
            elif multiplier == "Tsd.":
                ergebnis *= 1000
            else:
                raise ValueError()

        return ergebnis