#  Copyright (c) 2020 | KingKevin23 (@kingkevin023)

import re
from bs4 import BeautifulSoup
from datetime import datetime
from .ceo import Ceo
from .aktie import Aktie
from .anleihe import Anleihe, Kredit
from .zertifikat import Zertifikat
from .order import Order

class Ag:
    def __init__(self):
        self.wkn = None
        self.name = None
        self.gruendung = None
        self.aktienanzahl = None
        self.in_liquidation = None
        self.kurs = None
        self.brief = None
        self.geld = None
        self.brief_stueckzahl = None
        self.geld_stueckzahl = None
        self.sw_aktie = None
        self.bbw_aktie = None
        self.fp_aktie = None
        self.bw_aktie = None
        self.kurs_14d = None
        #TODO: self._kgv = None
        #TODO: self._spread = None
        #TODO: self._alter = None
        #TODO: self._tagesvolumen = None
        #TODO: self._boersenwert = None
        self.buchwert = None
        self.depotwert = None
        self.bargeld = None
        self.highscore = None
        self.highscore_groesse = None
        self.highscore_wachstum = None
        self.highscore_newcomer = None
        self.agsx_punkte = None
        self.in_agsx = None
        self.handelsaktivitaet = None
        self.ceo = None
        self.aktien = None
        self.anleihen = None
        self.kredite = None
        self.zertifikate = None
        self.orders = None

    @property
    def wkn(self) -> int:
        if self._wkn is None:
            self._wkn = int(self._api_data.get("wkn"))

        return self._wkn

    @wkn.setter
    def wkn(self, value:int):
        self._wkn = value

    @property
    def name(self) -> str:
        if self._name is None:
            self._name = self._api_data.get("name")

        return self._name

    @name.setter
    def name(self, value:str):
        self._name = value

    @property
    def gruendung(self) -> datetime:
        if self._gruendung is None:
            self._gruendung = datetime.strptime(self._api_data.get("gruendung"), "%Y-%m-%d %H:%M:%S")

        return self._gruendung

    @gruendung.setter
    def gruendung(self, value:datetime):
        self._gruendung = value

    @property
    def aktienanzahl(self) -> int:
        if self._aktienanzahl is None:
            self._aktienanzahl = int(self._api_data.get("aktienanzahl"))

        return self._aktienanzahl

    @aktienanzahl.setter
    def aktienanzahl(self, value:int):
        self._aktienanzahl = value

    @property
    def in_liquidation(self) -> bool:
        if self._in_liquidation is None:
            self._in_liquidation = self._api_data.get("in_liquidation") == "true"

        return self._in_liquidation

    @in_liquidation.setter
    def in_liquidation(self, value:bool):
        self._in_liquidation = value

    @property
    def kurs(self) -> float:
        if self._kurs is None:
            self._kurs = float(self._api_data.get("kurs"))

        return self._kurs

    @kurs.setter
    def kurs(self, value:float):
        self._kurs = value

    @property
    def brief(self) -> float:
        if self._brief is None:
            self._brief = float(self._api_data.get("brief"))

        return self._brief

    @brief.setter
    def brief(self, value:float):
        self._brief = value

    @property
    def geld(self) -> float:
        if self._geld is None:
            self._geld = float(self._api_data.get("geld"))

        return self._geld

    @geld.setter
    def geld(self, value:float):
        self._geld = value

    @property
    def brief_stueckzahl(self) -> int:
        if self._brief_stueckzahl is None:
            self._brief_stueckzahl = int(self._api_data.get("brief_stueckzahl"))

        return self._brief_stueckzahl

    @brief_stueckzahl.setter
    def brief_stueckzahl(self, value:int):
        self._brief_stueckzahl = value

    @property
    def geld_stueckzahl(self) -> int:
        if self._geld_stueckzahl is None:
            self._geld_stueckzahl = int(self._api_data.get("geld_stueckzahl"))

        return self._geld_stueckzahl

    @geld_stueckzahl.setter
    def geld_stueckzahl(self, value:int):
        self._geld_stueckzahl = value

    @property
    def sw_aktie(self) -> float:
        if self._sw_aktie is None:
            self._sw_aktie = self._web_data.find("div", attrs={"id":"sw"})
            self._sw_aktie = re.compile("\d*[.]?\d*[,]\d{2}").findall(self._sw_aktie.text)[0]
            self._sw_aktie = float(self._sw_aktie.replace(".", "").replace(",", "."))

        return self._sw_aktie

    @sw_aktie.setter
    def sw_aktie(self, value:float):
        self._sw_aktie = value

    @property
    def bbw_aktie(self) -> float:
        if self._bbw_aktie is None:
            self._bbw_aktie = self._web_data.find("div", attrs={"id": "bbw"})
            self._bbw_aktie = re.compile("\d*[.]?\d*[,]\d{2}").findall(self._bbw_aktie.text)[0]
            self._bbw_aktie = float(self._bbw_aktie.replace(".", "").replace(",", "."))

        return self._bbw_aktie

    @bbw_aktie.setter
    def bbw_aktie(self, value:float):
        self._bbw_aktie = value

    @property
    def fp_aktie(self) -> float:
        if self._fp_aktie is None:
            self._fp_aktie = self._web_data.find("div", attrs={"id": "fp"})
            self._fp_aktie = re.compile("\d*[.]?\d*[,]\d{2}").findall(self._fp_aktie.text)[0]
            self._fp_aktie = float(self._fp_aktie.replace(".", "").replace(",", "."))

        return self._fp_aktie

    @fp_aktie.setter
    def fp_aktie(self, value:float):
        self._fp_aktie = value

    @property
    def bw_aktie(self) -> float:
        if self._bw_aktie is None:
            self._bw_aktie = round(self.buchwert / self.aktienanzahl, 2)

        return self._bw_aktie

    @bw_aktie.setter
    def bw_aktie(self, value:float):
        self._bw_aktie = value

    @property
    def kurs_14d(self) -> float:
        if self._kurs_14d is None:
            self._kurs_14d = self._web_data.find("div", attrs={"id": "kurs14d"})
            self._kurs_14d = re.compile("[-]?\d*[.]?\d*[,]\d*").findall(self._kurs_14d.text)[0]
            self._kurs_14d = float(self._kurs_14d.replace(".", "").replace(",", "."))

        return self._kurs_14d

    @kurs_14d.setter
    def kurs_14d(self, value: str):
        self._kurs_14d = value

    @property
    def buchwert(self) -> float:
        if self._buchwert is None:
            self._buchwert = self.depotwert + self.bargeld

        return self._buchwert

    @buchwert.setter
    def buchwert(self, value:float):
        self._buchwert = value

    @property
    def depotwert(self) -> float:
        if self._depotwert is None:
            self._depotwert = float(self._api_data.get("depotwert"))

        return self._depotwert

    @depotwert.setter
    def depotwert(self, value:float):
        self._depotwert = value

    @property
    def bargeld(self) -> float:
        if self._bargeld is None:
            self._bargeld = float(self._api_data.get("bargeld"))

        return self._bargeld

    @bargeld.setter
    def bargeld(self, value:float):
        self._bargeld = value

    @property
    def highscore(self) -> int:
        if self._highscore is None:
            self._highscore = int(self._api_data.get("highscore_platz"))

        return self._highscore

    @highscore.setter
    def highscore(self, value:int):
        self._highscore = value

    @property
    def highscore_groesse(self) -> int:
        if self._highscore_groesse is None:
            self._highscore_groesse = int(self._api_data.get("highscore_platz_groesse"))

        return self._highscore_groesse

    @highscore_groesse.setter
    def highscore_groesse(self, value:int):
        self._highscore_groesse = value

    @property
    def highscore_wachstum(self) -> int:
        if self._highscore_wachstum is None:
            self._highscore_wachstum = int(self._api_data.get("highscore_platz_wachstum"))

        return self._highscore_wachstum

    @highscore_wachstum.setter
    def highscore_wachstum(self, value:int):
        self._highscore_wachstum = value

    @property
    def highscore_newcomer(self) -> int:
        if self._highscore_newcomer is None:
            self._highscore_newcomer = int(self._api_data.get("highscore_platz_newcomer"))

        return self._highscore_newcomer

    @highscore_newcomer.setter
    def highscore_newcomer(self, value:int):
        self._highscore_newcomer = value

    @property
    def agsx_punkte(self) -> int:
        if self._agsx_punkte is None:
            self._agsx_punkte = int(self._api_data.get("agsx_punkte"))

        return self._agsx_punkte

    @agsx_punkte.setter
    def agsx_punkte(self, value:int):
        self._agsx_punkte = value

    @property
    def in_agsx(self) -> bool:
        if self._in_agsx is None:
            self._in_agsx = self._api_data.get("in_agsx") == "true"

        return self._in_agsx

    @in_agsx.setter
    def in_agsx(self, value:bool):
        self._in_agsx = value

    @property
    def handelsaktivitaet(self) -> int:
        if self._handelsaktivitaet is None:
            self._handelsaktivitaet = int(self._api_data.get("handelsaktivitaet"))

        return self._handelsaktivitaet

    @handelsaktivitaet.setter
    def handelsaktivitaet(self, value:int):
        self._handelsaktivitaet = value

    @property
    def ceo(self) -> Ceo:
        if self._ceo is None:
            ceo_data:dict = self._api_data.get("ceo")
            index = self._web_data.find("img", attrs={"width":"150"}).attrs.get("title")
            index = re.compile("Spielerindex:.(.*)").findall(index)[0]
            self._ceo = Ceo(name=ceo_data.get("name"), index=index,
                            registrierung_datum=datetime.strptime(ceo_data.get("registrierung_datum"), "%Y-%m-%d %H:%M:%S"),
                            gesperrt=ceo_data.get("gesperrt")=="true", userprojekt=ceo_data.get("ist_userprojekt_account")=="true")

        return self._ceo

    @ceo.setter
    def ceo(self, value:Ceo):
        self._ceo = value

    @property
    def aktien(self) -> list:
        if self._aktien is None:
            self._aktien = []
            aktie: dict
            for aktie in self._api_data.get("aktien"):
                temp = Aktie(wkn=int(aktie.get("wkn")), stueckzahl=int(aktie.get("stueckzahl")))
                self._aktien.append(temp)

        return self._aktien

    @aktien.setter
    def aktien(self, value:list):
        self._aktien = value

    @property
    def anleihen(self) -> list:
        if self._anleihen is None:
            self._anleihen = []
            anleihe: dict
            for anleihe in self._api_data.get("anleihen"):
                temp = Anleihe(betrag=int(anleihe.get("betrag")), zins=float(anleihe.get("zins")),
                               auszahlung_datum=datetime.strptime(anleihe.get("auszahlung_datum"), "%Y-%m-%d %H:%M:%S"),
                               laufzeit=int(anleihe.get("laufzeit")))
                self._anleihen.append(temp)

        return self._anleihen

    @anleihen.setter
    def anleihen(self, value:list):
        self._anleihen = value

    @property
    def kredite(self) -> list:
        if self._kredite is None:
            self._kredite = []
            kredit: dict
            for kredit in self._api_data.get("kredite"):
                temp = Kredit(betrag=int(kredit.get("betrag")), zins=float(kredit.get("zins")),
                              rueckzahlung_datum=datetime.strptime(kredit.get("rueckzahlung_datum"), "%Y-%m-%d %H:%M:%S"),
                              laufzeit=int(kredit.get("laufzeit")))
                self._kredite.append(temp)

        return self._kredite

    @kredite.setter
    def kredite(self, value:list):
        self._kredite = value

    @property
    def zertifikate(self) -> list:
        if self._zertifikate is None:
            self._zertifikate = []
            zertifikat: dict
            for zertifikat in self._api_data.get("zertifikate"):
                temp = Zertifikat(betrag=float(zertifikat.get("betrag")), typ=zertifikat.get("typ"),
                                  hebel=float(zertifikat.get("hebel")), punkte=int(zertifikat.get("punkte")),
                                  ablaufdatum=datetime.strptime(zertifikat.get("ablauf_datum"), "%Y-%m-%d %H:%M:%S"))
                self._zertifikate.append(temp)

        return self._zertifikate

    @zertifikate.setter
    def zertifikate(self, value:list):
        self._zertifikate = value

    @property
    def orders(self) -> list:
        if self._orders is None:
            self._orders = []
            order: dict
            for order in self._api_data.get("orders"):
                temp = Order(typ=order.get("typ"), limit=float(order.get("limit")),
                             stueckzahl=int(order.get("stueckzahl")),
                             orderregel=order.get("orderregel") == "true",
                             systembank=order.get("systembank_order") == "true",
                             datum=datetime.strptime(order.get("datum"), "%Y-%m-%d %H:%M:%S"))
                self._orders.append(temp)

        return self._orders

    @orders.setter
    def orders(self, value:list):
        self._orders = value