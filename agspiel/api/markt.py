#  Copyright (c) 2020 | KingKevin23 (@kingkevin023)

class Markt:
    def __init__(self, ags:int=None, orders_24:int=None, volumen_24:float=None, agsx_punkte:int=None,
                 agsx_aenderung:int=None, put_hebel:float=None, call_hebel:float=None, anleihenzins:float=None):
        self.ags:int = ags
        self.orders_24:int = orders_24
        self.volumen_24:float = volumen_24
        self.agsx_punkte:int = agsx_punkte
        self.agsx_aenderung:int = agsx_aenderung
        self.put_hebel:float = put_hebel
        self.call_hebel:float = call_hebel
        self.anleihenzins:float = anleihenzins

    @property
    def ags(self) -> int:
        return self._ags

    @ags.setter
    def ags(self, value:int):
        self._ags = value

    @property
    def orders_24(self) -> int:
        return self._orders_24

    @orders_24.setter
    def orders_24(self, value:int):
        self._orders_24 = value

    @property
    def volumen_24(self) -> float:
        return self._volumen_24

    @volumen_24.setter
    def volumen_24(self, value:float):
        self._volumen_24 = value

    @property
    def agsx_punkte(self) -> int:
        return self._agsx_punkte

    @agsx_punkte.setter
    def agsx_punkte(self, value:int):
        self._agsx_punkte = value

    @property
    def agsx_aenderung(self) -> int:
        return self._agsx_aenderung

    @agsx_aenderung.setter
    def agsx_aenderung(self, value:int):
        self._agsx_aenderung = value

    @property
    def put_hebel(self) -> float:
        return self._put_hebel

    @put_hebel.setter
    def put_hebel(self, value:float):
        self._put_hebel = value

    @property
    def call_hebel(self) -> float:
        return self._call_hebel

    @call_hebel.setter
    def call_hebel(self, value:float):
        self._call_hebel = value

    @property
    def anleihenzins(self) -> float:
        return self._anleihenzins

    @anleihenzins.setter
    def anleihenzins(self, value:float):
        self._anleihenzins = value