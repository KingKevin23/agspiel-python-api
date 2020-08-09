#  Copyright (c) 2020 | KingKevin23 (@kingkevin023)

class Aktie:
    def __init__(self, wkn:int, stueckzahl:int):
        self.wkn:int = wkn
        self.stueckzahl:int = stueckzahl

    @property
    def wkn(self) -> int:
        return self._wkn

    @wkn.setter
    def wkn(self, value:int):
        self._wkn = value

    @property
    def stueckzahl(self) -> int:
        return self._stueckzahl

    @stueckzahl.setter
    def stueckzahl(self, value:int):
        self._stueckzahl = value

class Aktionaer(Aktie):
    def __init__(self, wkn: int, stueckzahl: int):
        super().__init__(wkn, stueckzahl)