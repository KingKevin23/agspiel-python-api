#  Copyright (c) 2020 | KingKevin23 (@kingkevin023)

from datetime import datetime
from .ceo import Ceo
from .aktie import Aktie
from .anleihe import Anleihe, Kredit
from .zertifikat import Zertifikat
from .order import Order

class Ag:
    def __init__(self, api_data:dict, web_data:str):
        self._api_data:dict = api_data
        self._web_data:str = web_data
        self._wkn:int = None
        self._name:str = None
        self._gruendung:datetime = None
        self._aktienanzahl:int = None
        self._in_liquidation:bool = None
        self._kurs:float = None
        self._brief:float = None
        self._geld:float = None
        self._brief_stueckzahl:int = None
        self._geld_stueckzahl:int = None
        self._depotwert:float = None
        self._bargeld:float = None
        self._highscore:int = None
        self._highscore_groesse:int = None
        self._highscore_wachstum:int = None
        self._highscore_newcomer:int = None
        self._agsx_punkte:int = None
        self._in_agsx:bool = None
        self._handelsaktivitaet:int = None
        self._ceo:Ceo = None
        self._aktien:list = None
        self._anleihen:list = None
        self._kredite:list = None
        self._zertifikate:list = None
        self._orders:list = None

    @property
    def wkn(self) -> int:
        if self._wkn is None:
            self._wkn = int(self._api_data.get("wkn"))

        return self._wkn

    @property
    def name(self) -> str:
        if self._name is None:
            self._name = self._api_data.get("name")

        return self._name

    @property
    def gruendung(self) -> datetime:
        if self._gruendung is None:
            self._gruendung = datetime.strptime(self._api_data.get("gruendung"), "%Y-%m-%d %H:%M:%S")

        return self._gruendung

    @property
    def aktienanzahl(self) -> int:
        if self._aktienanzahl is None:
            self._aktienanzahl = int(self._api_data.get("aktienanzahl"))

        return self._aktienanzahl

    @property
    def in_liquidation(self) -> bool:
        if self._in_liquidation is None:
            self._in_liquidation = self._api_data.get("in_liquidation") == "true"

        return self._in_liquidation

    @property
    def kurs(self) -> float:
        if self._kurs is None:
            self._kurs = float(self._api_data.get("kurs"))

        return self._kurs

    @property
    def brief(self) -> float:
        if self._brief is None:
            self._brief = float(self._api_data.get("brief"))

        return self._brief

    @property
    def geld(self) -> float:
        if self._geld is None:
            self._geld = float(self._api_data.get("geld"))

        return self._geld

    @property
    def brief_stueckzahl(self) -> int:
        if self._brief_stueckzahl is None:
            self._brief_stueckzahl = int(self._api_data.get("brief_stueckzahl"))

        return self._brief_stueckzahl

    @property
    def geld_stueckzahl(self) -> int:
        if self._geld_stueckzahl is None:
            self._geld_stueckzahl = int(self._api_data.get("geld_stueckzahl"))

        return self._geld_stueckzahl

    @property
    def depotwert(self) -> float:
        if self._depotwert is None:
            self._depotwert = float(self._api_data.get("depotwert"))

        return self._depotwert

    @property
    def bargeld(self) -> float:
        if self._bargeld is None:
            self._bargeld = float(self._api_data.get("bargeld"))

        return self._bargeld

    @property
    def highscore(self) -> int:
        if self._highscore is None:
            self._highscore = int(self._api_data.get("highscore_platz"))

        return self._highscore

    @property
    def highscore_groesse(self) -> int:
        if self._highscore_groesse is None:
            self._highscore_groesse = int(self._api_data.get("highscore_platz_groesse"))

        return self._highscore_groesse

    @property
    def highscore_wachstum(self) -> int:
        if self._highscore_wachstum is None:
            self._highscore_wachstum = int(self._api_data.get("highscore_platz_wachstum"))

        return self._highscore_wachstum

    @property
    def highscore_newcomer(self) -> int:
        if self._highscore_newcomer is None:
            self._highscore_newcomer = int(self._api_data.get("highscore_platz_newcomer"))

        return self._highscore_newcomer

    @property
    def agsx_punkte(self) -> int:
        if self._agsx_punkte is None:
            self._agsx_punkte = int(self._api_data.get("agsx_punkte"))

        return self._agsx_punkte

    @property
    def in_agsx(self) -> bool:
        if self._in_agsx is None:
            self._in_agsx = self._api_data.get("in_agsx") == "true"

        return self._in_agsx

    @property
    def handelsaktivitaet(self) -> int:
        if self._handelsaktivitaet is None:
            self._handelsaktivitaet = int(self._api_data.get("handelsaktivitaet"))

        return self._handelsaktivitaet

    @property
    def ceo(self) -> Ceo:
        if self._ceo is None:
            ceo_data:dict = self._api_data.get("ceo")
            self._ceo = Ceo(name=ceo_data.get("name"),
                            registrierung_datum=datetime.strptime(ceo_data.get("registrierung_datum"), "%Y-%m-%d %H:%M:%S"),
                            gesperrt=ceo_data.get("gesperrt")=="true", userprojekt=ceo_data.get("ist_userprojekt_account")=="true")

        return self._ceo

    @property
    def aktien(self) -> list:
        if self._aktien is None:
            self._aktien = []
            aktie: dict
            for aktie in self._api_data.get("aktien"):
                temp = Aktie(wkn=int(aktie.get("wkn")), stueckzahl=int(aktie.get("stueckzahl")))
                self._aktien.append(temp)

        return self._aktien

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