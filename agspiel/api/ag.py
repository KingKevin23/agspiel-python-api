#  Copyright (c) 2021 | KingKevin23 (@kingkevin023)

import re
from datetime import datetime, date
from bs4 import BeautifulSoup

from .aktie import Aktie, Aktionaer
from .anleihe import Anleihe, Kredit
from .ceo import Ceo
from .data import Data
from .index import Index
from .kapitalmassnahme import Kapitalerhoehung, Kapitalherabsetzung
from .order import Order
from .zertifikat import Zertifikat


class Ag:
    def __init__(self, wkn: int, api_data: Data, web_data: Data, chronik_data: Data):
        self._wkn: int = wkn
        self._api_data: Data = api_data
        self._web_data: Data = web_data
        self._chronik_data: Data = chronik_data
        self._ag_data = lambda: self._api_data().get("ags").get(str(self.wkn))

    @property
    def wkn(self) -> int:
        return self._wkn

    @property
    def name(self) -> str:
        return self._ag_data().get("name")

    @property
    def logo(self) -> str:
        return "https://www.ag-spiel.de/" + self._web_data().find(id="logocontainer").img.attrs["src"]

    @property
    def gruendung(self) -> datetime:
        return datetime.strptime(self._ag_data().get("gruendung"), "%Y-%m-%d %H:%M:%S")

    @property
    def aktienanzahl(self) -> int:
        return int(self._ag_data().get("aktienanzahl"))

    @property
    def in_liquidation(self) -> bool:
        return self._ag_data().get("in_liquidation")

    @property
    def in_kapitalerhoehung(self) -> bool:
        return self._ag_data().get("laufende_ke")

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
        return float(
            re.compile("-?(?:\d{,3}[.])*\d{,3}[,]\d{2}").findall(self._web_data().find("div", attrs={"id": "sw"}).text)[0]
            .replace(".", "").replace(",", "."))

    @property
    def bbw_aktie(self) -> float:
        return float(
            re.compile("-?(?:\d{,3}[.])*\d{,3}[,]\d{2}").findall(self._web_data().find("div", attrs={"id": "bbw"}).text)[0]
            .replace(".", "").replace(",", "."))

    @property
    def fp_aktie(self) -> float:
        return float(
            re.compile("-?(?:\d{,3}[.])*\d{,3}[,]\d{2}").findall(self._web_data().find("div", attrs={"id": "fp"}).text)[0]
            .replace(".", "").replace(",", "."))

    @property
    def bw_aktie(self) -> float:
        return round(self.buchwert / self.aktienanzahl, 2)

    @property
    def kgv(self) -> float:
        return float(re.compile("\d*[,]\d*").findall(self._web_data().find("div", attrs={"id": "kgv"}).text)[0].
                     replace(",", "."))
    
    @property
    def live_kurs_14d(self)-> float:
        return float(re.compile("\d*[,]\d*|(n/a)").findall(self._web_data().find("div", attrs={"id": "kurs14d"}).text)[0].
                     replace(",", ".").replace("n/a","0"))

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
        return Ag._convert_number(self._web_data().find("div", attrs={"id": "tagesvolumen"}).text)

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
        return self._ag_data().get("in_agsx")

    @property
    def handelsaktivitaet(self) -> int:
        return int(self._ag_data().get("handelsaktivitaet"))

    @property
    def ceo(self) -> Ceo:
        name = self._ag_data().get("ceo").get("name")

        # Alles zum Index
        try:
            index_id = int(self._ag_data().get("index_id"))
            index_data = self._api_data().get("indizes").get(str(index_id))
            index_name = index_data.get("name")
            index_highscore = int(index_data.get("highscore_platz"))
            index_punkte = int(index_data.get("punkte"))
            index_gruendung = datetime.strptime(index_data.get("gruendung_datum"), "%Y-%m-%d %H:%M:%S")
            index = Index(nummer=index_id, name=index_name, highscore=index_highscore, punkte=index_punkte,
                          gruendung_datum=index_gruendung)
        except TypeError:  # Wenn Spieler in keinem Index
            index = None

        registrierung_datum = datetime.strptime(self._ag_data().get("ceo").get("registrierung_datum"),
                                                "%Y-%m-%d %H:%M:%S")
        gesperrt = self._ag_data().get("ceo").get("gesperrt")
        premium = self._ag_data().get("ceo").get("premium")
        userprojekt = self._ag_data().get("ceo").get("ist_userprojekt_account")
        return Ceo(name=name, index=index, registrierung_datum=registrierung_datum, gesperrt=gesperrt,
                   premium=premium, userprojekt=userprojekt)

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
            except TypeError:  # falls hebel noch nicht bekannt
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
                         orderregel=i.get("orderregel"), systembank=i.get("systembank_order"),
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
    def kes(self) -> list:
        kes = []
        rows = self._chronik_data().find("table", attrs={"id": "kes"}).find_all("tr")
        for row in rows:
            cols = row.find_all("td")
            if len(cols) > 0:
                if cols[0].text != "Gesamt":
                    datum: date = datetime.strptime(cols[0].text, "%d.%m.%Y").date()
                    anzahl, preis, gesamt = None, None, None
                    if cols[1].text != "n/a":
                        anzahl = int(cols[1].text.replace(".", ""))

                    if cols[2].text != "n/a":
                        preis = float(cols[2].text.replace(".", "").replace(",", ".").replace("€", "").strip())

                    if cols[3].text != "n/a":
                        gesamt = float(cols[3].text.replace(".", "").replace(",", ".").replace("€", "").strip())
                    kes.append(Kapitalerhoehung(datum, anzahl, preis, gesamt))

        return kes

    @property
    def khs(self) -> list:
        khs = []
        rows = self._chronik_data().find("table", attrs={"id": "khs"}).find_all("tr")
        for row in rows:
            cols = row.find_all("td")
            if len(cols) > 0:
                if cols[0].text != "Gesamt":
                    datum: date = datetime.strptime(cols[0].text, "%d.%m.%Y").date()
                    anzahl, preis, gesamt = None, None, None
                    if cols[1].text != "n/a":
                        anzahl = int(cols[1].text.replace(".", ""))

                    if cols[2].text != "n/a":
                        preis = float(cols[2].text.replace(".", "").replace(",", ".").replace("€", "").strip())

                    if cols[3].text != "n/a":
                        gesamt = float(cols[3].text.replace(".", "").replace(",", ".").replace("€", "").strip())
                    khs.append(Kapitalherabsetzung(datum, anzahl, preis, gesamt))

        return khs

    @property
    def dividende(self) -> float:
        return float(self._ag_data().get("dividende"))

    @property
    def max_zertis(self) -> int:
        return int(float(self._ag_data().get("max_zertifikate_anteil")) * 100)

    @property
    def max_zertis_aenderbar(self) -> bool:
        return self._ag_data().get("max_zertifikate_anteil_aenderbar")

    @property
    def uebernahmeschutz(self) -> bool:
        return self._ag_data().get("uebernahmeschutz")

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
        return self._get_table_data()[0]

    @property
    def kurs_30d(self) -> float:
        return self._get_table_data()[1]

    @property
    def kurs_60d(self) -> float:
        return self._get_table_data()[2]

    @property
    def kurs_90d(self) -> float:
        return self._get_table_data()[3]

    @property
    def bw_14d(self) -> float:
        return self._get_table_data()[4]

    @property
    def bw_30d(self) -> float:
        return self._get_table_data()[5]

    @property
    def bw_60d(self) -> float:
        return self._get_table_data()[6]

    @property
    def bw_90d(self) -> float:
        return self._get_table_data()[7]

    @property
    def fp_14d(self) -> float:
        return self._get_table_data()[8]

    @property
    def fp_30d(self) -> float:
        return self._get_table_data()[9]

    @property
    def fp_60d(self) -> float:
        return self._get_table_data()[10]

    @property
    def fp_90d(self) -> float:
        return self._get_table_data()[11]

    @property
    def ordner(self) -> str:
        try:
            return re.compile("Ordner:\s(.*)Deine\sNotiz:").findall(
                self._web_data().find("div", attrs={"class": "nodisplay profil-depotcomment"})
                .text)[0]
        except AttributeError:
            return "Allgemein"

    @property
    def kauf_kurs(self) -> float:
        try:
            return float(
                re.compile("Kauf:\s((?:\d*[.,]?)*)\s€").findall(self._web_data().find("div", attrs={"id": "imdepot"})
                                                                .text)[0].replace(".", "").replace(",", "."))
        except AttributeError:
            return None

    @property
    def kauf_anzahl(self) -> int:
        try:
            return int(re.compile("In\sdeinem\sDepot:((?:\d*\.?)*)\sStk\.").findall(
                self._web_data().find("div", attrs={"id": "imdepot"})
                .text)[0].replace(".", ""))
        except AttributeError:
            return 0

    def _get_table_data(self):
        table_data = []
        rows = self._web_data().find('table', attrs={'class': 'normalborder'}).find_all('tr')
        for row in rows:
            cols = row.find_all("td")
            if len(cols) >= 2:
                # Nur hier stehen Werte
                last_col = str(cols[len(cols) - 1])
                regex = re.findall(">-?\d*.?\d*,\d*<", last_col)
                try:
                    table_data.append(float(regex[0][1:-1].replace(".", "").replace(",", ".")))
                except IndexError:
                    table_data.append(None)

        return table_data

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