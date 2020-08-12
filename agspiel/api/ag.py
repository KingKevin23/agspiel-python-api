#  Copyright (c) 2020 | KingKevin23 (@kingkevin023)

from datetime import datetime
from .ceo import Ceo

class Ag:
    def __init__(self, wkn:int=None, name:str=None, gruendung:datetime=None, aktienanzahl:int=None,
                 in_liquidation:bool=None, kurs:float=None, brief:float=None, geld:float=None, brief_stueckzahl:int=None,
                 geld_stueckzahl:int=None, sw_aktie:float=None, bbw_aktie:float=None, fp_aktie:float=None,
                 kurs_14d:float=None, kgv:float=None, tagesvolumen:float=None, depotwert:float=None,
                 bargeld:float=None, highscore:int=None,  highscore_groesse:int=None, highscore_wachstum:int=None,
                 highscore_newcomer:int=None, agsx_punkte:int=None, in_agsx:bool=None, handelsaktivitaet:int=None,
                 ceo:Ceo=None, aktien:list=None, anleihen:list=None, kredite:list=None, zertifikate:list=None,
                 orders:list=None):
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
        self.sw_aktie:float = sw_aktie
        self.bbw_aktie:float = bbw_aktie
        self.fp_aktie:float = fp_aktie
        self.kurs_14d:float = kurs_14d
        self.kgv:float = kgv
        self.tagesvolumen:float = tagesvolumen
        self.depotwert:float = depotwert
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
        self.zertifikate:list = zertifikate
        self.orders:list = orders

        # Hier werden alle Kennzahlen initialisiert, die aus anderen berechnet werden können:
        self.alter:int = (datetime.now() - self.gruendung).days
        self.boersenwert:float = self.kurs * self.aktienanzahl
        self.buchwert: float = self.depotwert + self.bargeld
        self.spread: float = 1 - (self.geld / self.brief)
        self.bw_aktie: float = round(self.buchwert / self.aktienanzahl, 2)

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
    def kgv(self) -> float:
        return self._kgv

    @kgv.setter
    def kgv(self, value:float):
        self._kgv = value

    @property
    def spread(self) -> float:
        return self._spread

    @spread.setter
    def spread(self, value:float):
        self._spread = value

    @property
    def alter(self) -> int:
        return self._alter

    @alter.setter
    def alter(self, value:int):
        self._alter = value

    @property
    def tagesvolumen(self) -> float:
        return self._tagesvolumen

    @tagesvolumen.setter
    def tagesvolumen(self, value:float):
        self._tagesvolumen = value

    @property
    def boersenwert(self) -> float:
        return self._tagesvolumen

    @boersenwert.setter
    def boersenwert(self, value:float):
        self._boersenwert = value

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