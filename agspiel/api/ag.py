#  Copyright (c) 2020 | KingKevin23 (@kingkevin023)

from datetime import datetime
from .ceo import Ceo
from .data import Data

class Ag:
    def __init__(self, wkn:int, api_data:Data, web_data:Data):
        self._wkn:int = wkn
        self.api_data:Data = api_data
        self.web_data:Data = web_data

    @property
    def wkn(self) -> int:
        return self._wkn

    @property
    def name(self) -> str:
        return self._name

    @property
    def gruendung(self) -> datetime:
        return self._gruendung

    @property
    def aktienanzahl(self) -> int:
        return self._aktienanzahl

    @property
    def in_liquidation(self) -> bool:
        return self._in_liquidation

    @property
    def kurs(self) -> float:
        return self._kurs

    @property
    def brief(self) -> float:
        return self._brief

    @property
    def geld(self) -> float:
        return self._geld

    @property
    def brief_stueckzahl(self) -> int:
        return self._brief_stueckzahl

    @property
    def geld_stueckzahl(self) -> int:
        return self._geld_stueckzahl

    @property
    def sw_aktie(self) -> float:
        return self._sw_aktie

    @property
    def bbw_aktie(self) -> float:
        return self._bbw_aktie

    @property
    def fp_aktie(self) -> float:
        return self._fp_aktie

    @property
    def bw_aktie(self) -> float:
        return round(self.buchwert / self.aktienanzahl, 2)

    @property
    def kgv(self) -> float:
        return self._kgv

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
        return self._tagesvolumen

    @property
    def boersenwert(self) -> float:
        return self.kurs * self.aktienanzahl

    @property
    def buchwert(self) -> float:
        return self.depotwert + self.bargeld

    @property
    def depotwert(self) -> float:
        return self._depotwert

    @property
    def bargeld(self) -> float:
        return self._bargeld

    @property
    def highscore(self) -> int:
        return self._highscore

    @property
    def highscore_groesse(self) -> int:
        return self._highscore_groesse

    @property
    def highscore_wachstum(self) -> int:
        return self._highscore_wachstum

    @property
    def highscore_newcomer(self) -> int:
        return self._highscore_newcomer

    @property
    def agsx_punkte(self) -> int:
        return self._agsx_punkte

    @property
    def in_agsx(self) -> bool:
        return self._in_agsx

    @property
    def handelsaktivitaet(self) -> int:
        return self._handelsaktivitaet

    @property
    def ceo(self) -> Ceo:
        return self._ceo

    @property
    def aktien(self) -> list:
        return self._aktien

    @property
    def anleihen(self) -> list:
        return self._anleihen

    @property
    def kredite(self) -> list:
        return self._kredite

    @property
    def zertifikate(self) -> list:
        return self._zertifikate

    @property
    def orders(self) -> list:
        return self._orders

    @property
    def dividende(self) -> float:
        return self._dividende

    @property
    def max_zertis(self) -> int:
        return self._max_zertis

    @property
    def tages_hoch(self) -> float:
        return self._tages_hoch

    @property
    def tages_tief(self) -> float:
        return self._tages_tief

    @property
    def kurs_14d(self) -> float:
        return self._kurs_14d

    @property
    def kurs_30d(self) -> float:
        return self._kurs_30d

    @property
    def kurs_60d(self) -> float:
        return self._kurs_60d

    @property
    def kurs_90d(self) -> float:
        return self._kurs_90d

    @property
    def bw_14d(self) -> float:
        return self._bw_14d

    @property
    def bw_30d(self) -> float:
        return self._bw_30d

    @property
    def bw_60d(self) -> float:
        return self._bw_60d

    @property
    def bw_90d(self) -> float:
        return self._bw_90d

    @property
    def fp_14d(self) -> float:
        return self._fp_14d

    @property
    def fp_30d(self) -> float:
        return self._fp_30d

    @property
    def fp_60d(self) -> float:
        return self._fp_60d

    @property
    def fp_90d(self) -> float:
        return self._fp_90d