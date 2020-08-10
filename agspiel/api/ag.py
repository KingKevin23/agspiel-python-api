#  Copyright (c) 2020 | KingKevin23 (@kingkevin023)

from datetime import datetime
from .ceo import Ceo
from .aktie import Aktie
from .anleihe import Anleihe, Kredit
from .zertifikat import Zertifikat
from .order import Order

class Ag:
    def __init__(self, wkn:int, name:str, gruendung:datetime, aktienanzahl:int, in_liquidation:bool, kurs:float,
                 brief:float, geld:float, brief_stueckzahl:int, geld_stueckzahl:int, depotwert:float, bargeld:float,
                 highscore:int, highscore_groesse:int, highscore_wachstum:int, highscore_newcomer:int,
                 agsx_punkte:int, in_agsx:bool, handelsaktivitaet:int, ceo:Ceo, aktien:list, anleihen:list,
                 kredite:list, zertifikate:list, orders:list):
        self.wkn:int = wkn
        self.name:str = name
        self.gruendung:datetime = gruendung
        self.aktienanzahl:int = aktienanzahl
        self.in_liquidation:bool = in_liquidation
        self.kurs:float = kurs
        self.brief:float = brief
        self.geld:float = geld
        self.brief_stueckzahl:int = brief_stueckzahl
        self.geld_stueckzahl:int = geld_stueckzahl
        self.depotwert:float= depotwert
        self.bargeld:float = bargeld
        self.highscore:int = highscore
        self.highscore_groesse:int = highscore_groesse
        self.highscore_wachstum:int = highscore_wachstum
        self.highscore_newcomer:int = highscore_newcomer
        self.agsx_punkte:int = agsx_punkte
        self.in_agsx:bool = in_agsx
        self.handelsaktivitaet:int = handelsaktivitaet
        self.ceo:Ceo = ceo
        self.aktien:list = aktien
        self.anleihen:list = anleihen
        self.kredite:list = kredite
        self.zertifikate:list= zertifikate
        self.orders:list = orders

    @property
    def wkn(self) -> int:
        return self._wkn

    @wkn.setter
    def wkn(self, value:int):
        self._wkn = value

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value:str):
        self._name = value

    @property
    def gruendung(self) -> datetime:
        return self._gruendung

    @gruendung.setter
    def gruendung(self, value:datetime):
        self._gruendung = value

    @property
    def aktienanzahl(self) -> int:
        return self._aktienanzahl

    @aktienanzahl.setter
    def aktienanzahl(self, value:int):
        self._aktienanzahl = value

    @property
    def in_liquidation(self) -> bool:
        return self._in_liquidation

    @in_liquidation.setter
    def in_liquidation(self, value:bool):
        self._in_liquidation = value

    @property
    def kurs(self) -> float:
        return self._kurs

    @kurs.setter
    def kurs(self, value:float):
        self._kurs = value

    @property
    def brief(self) -> float:
        return self._brief

    @brief.setter
    def brief(self, value:float):
        self._brief = value

    @property
    def geld(self) -> float:
        return self._geld

    @geld.setter
    def geld(self, value:float):
        self._geld = value

    @property
    def brief_stueckzahl(self) -> int:
        return self._brief_stueckzahl

    @brief_stueckzahl.setter
    def brief_stueckzahl(self, value:int):
        self._brief_stueckzahl = value

    @property
    def geld_stueckzahl(self) -> int:
        return self._geld_stueckzahl

    @geld_stueckzahl.setter
    def geld_stueckzahl(self, value:int):
        self._geld_stueckzahl = value

    @property
    def depotwert(self) -> float:
        return self._depotwert

    @depotwert.setter
    def depotwert(self, value:float):
        self._depotwert = value

    @property
    def bargeld(self) -> float:
        return self._bargeld

    @bargeld.setter
    def bargeld(self, value:float):
        self._bargeld = value

    @property
    def highscore(self) -> int:
        return self._highscore

    @highscore.setter
    def highscore(self, value:int):
        self._highscore = value

    @property
    def highscore_groesse(self) -> int:
        return self._highscore_groesse

    @highscore_groesse.setter
    def highscore_groesse(self, value:int):
        self._highscore_groesse = value

    @property
    def highscore_wachstum(self) -> int:
        return self._highscore_wachstum

    @highscore_wachstum.setter
    def highscore_wachstum(self, value:int):
        self._highscore_wachstum = value

    @property
    def highscore_newcomer(self) -> int:
        return self._highscore_newcomer

    @highscore_newcomer.setter
    def highscore_newcomer(self, value:int):
        self._highscore_newcomer = value

    @property
    def agsx_punkte(self) -> int:
        return self._agsx_punkte

    @agsx_punkte.setter
    def agsx_punkte(self, value:int):
        self._agsx_punkte = value

    @property
    def in_agsx(self) -> bool:
        return self._in_agsx

    @in_agsx.setter
    def in_agsx(self, value:bool):
        self._in_agsx = value

    @property
    def handelsaktivitaet(self) -> int:
        return self._handelsaktivitaet

    @handelsaktivitaet.setter
    def handelsaktivitaet(self, value:int):
        self._handelsaktivitaet = value

    @property
    def ceo(self) -> Ceo:
        return self._ceo

    @ceo.setter
    def ceo(self, value:Ceo):
        self._ceo = value

    @property
    def aktien(self) -> list:
        if type(self._aktien[0]) is not Aktie:
            temp_list = []
            aktie: dict
            for aktie in self._aktien:
                temp = Aktie(wkn=int(aktie.get("wkn")), stueckzahl=int(aktie.get("stueckzahl")))
                temp_list.append(temp)
            self._aktien = temp_list

        return self._aktien

    @aktien.setter
    def aktien(self, value:list):
        self._aktien = value

    @property
    def anleihen(self) -> list:
        if type(self._anleihen[0]) is not Anleihe:
            temp_list = []
            anleihe: dict
            for anleihe in self._anleihen:
                temp = Anleihe(betrag=int(anleihe.get("betrag")), zins=float(anleihe.get("zins")),
                               auszahlung_datum=datetime.strptime(anleihe.get("auszahlung_datum"), "%Y-%m-%d %H:%M:%S"),
                               laufzeit=int(anleihe.get("laufzeit")))
                temp_list.append(temp)
            self._anleihen = temp_list

        return self._anleihen

    @anleihen.setter
    def anleihen(self, value:list):
        self._anleihen = value

    @property
    def kredite(self) -> list:
        if type(self._kredite[0]) is not Kredit:
            temp_list = []
            kredit: dict
            for kredit in self._kredite:
                temp = Kredit(betrag=int(kredit.get("betrag")), zins=float(kredit.get("zins")),
                               rueckzahlung_datum=datetime.strptime(kredit.get("auszahlung_datum"), "%Y-%m-%d %H:%M:%S"),
                               laufzeit=int(kredit.get("laufzeit")))
                temp_list.append(temp)
            self._kredite = temp_list

        return self._kredite

    @kredite.setter
    def kredite(self, value:list):
        self._kredite = value

    @property
    def zertifikate(self) -> list:
        if type(self._zertifikate[0]) is not Zertifikat:
            temp_list = []
            zertifikat: dict
            for zertifikat in self._zertifikate:
                temp = Zertifikat(betrag=float(zertifikat.get("betrag")), typ=zertifikat.get("typ"),
                                  hebel=float(zertifikat.get("hebel")), punkte=int(zertifikat.get("punkte")),
                                  ablaufdatum=datetime.strptime(zertifikat.get("ablauf_datum"), "%Y-%m-%d %H:%M:%S"))
                temp_list.append(temp)
            self._zertifikate = temp_list

        return self._zertifikate

    @zertifikate.setter
    def zertifikate(self, value:list):
        self._zertifikate = value

    @property
    def orders(self) -> list:
        if type(self._orders[0]) is not Order:
            temp_list = []
            order: dict
            for order in self._orders:
                temp = Order(typ=order.get("typ"), limit=float(order.get("limit")), stueckzahl=int(order.get("stueckzahl")),
                             orderregel=order.get("orderregel")=="true", systembank=order.get("systembank_order")=="true",
                             datum=datetime.strptime(order.get("datum"), "%Y-%m-%d %H:%M:%S"))
                temp_list.append(temp)
            self._orders = temp_list

        return self._orders

    @orders.setter
    def orders(self, value:list):
        self._orders = value