#  Copyright (c) 2020 | KingKevin23 (@kingkevin023)

from datetime import datetime
from .ceo import Ceo

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
    def sw_aktie(self) -> float:
        return self._sw_aktie

    @sw_aktie.setter
    def sw_aktie(self, value:float):
        self._sw_aktie = value

    @property
    def bbw_aktie(self) -> float:
        return self._bbw_aktie

    @bbw_aktie.setter
    def bbw_aktie(self, value:float):
        self._bbw_aktie = value

    @property
    def fp_aktie(self) -> float:
        return self._fp_aktie

    @fp_aktie.setter
    def fp_aktie(self, value:float):
        self._fp_aktie = value

    @property
    def bw_aktie(self) -> float:
        return self._bw_aktie

    @bw_aktie.setter
    def bw_aktie(self, value:float):
        self._bw_aktie = value

    @property
    def kurs_14d(self) -> float:
        return self._kurs_14d

    @kurs_14d.setter
    def kurs_14d(self, value:float):
        self._kurs_14d = value

    @property
    def buchwert(self) -> float:
        return self._buchwert

    @buchwert.setter
    def buchwert(self, value:float):
        self._buchwert = value

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
        return self._aktien

    @aktien.setter
    def aktien(self, value:list):
        self._aktien = value

    @property
    def anleihen(self) -> list:
        return self._anleihen

    @anleihen.setter
    def anleihen(self, value:list):
        self._anleihen = value

    @property
    def kredite(self) -> list:
        return self._kredite

    @kredite.setter
    def kredite(self, value:list):
        self._kredite = value

    @property
    def zertifikate(self) -> list:
        return self._zertifikate

    @zertifikate.setter
    def zertifikate(self, value:list):
        self._zertifikate = value

    @property
    def orders(self) -> list:
        return self._orders

    @orders.setter
    def orders(self, value:list):
        self._orders = value