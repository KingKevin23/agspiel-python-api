#  Copyright (c) 2021 | KingKevin23 (@kingkevin023)

from datetime import date

class _Kapitalmassnahme:
    def __init__(self, datum:date, stueckzahl:int, kurs:float, summe:float):
        self._datum:date = datum
        self._stueckzahl:int = stueckzahl
        self._kurs:float = kurs
        self._summe:float = summe

    @property
    def datum(self) -> date:
        return self._datum

    @datum.setter
    def datum(self, datum:date):
        self._datum = datum

    @property
    def stueckzahl(self) -> int:
        return self._stueckzahl

    @stueckzahl.setter
    def stueckzahl(self, stueckzahl: int):
        self._stueckzahl = stueckzahl

    @property
    def kurs(self) -> float:
        return self._kurs

    @kurs.setter
    def kurs(self, kurs: float):
        self._kurs = kurs

    @property
    def summe(self) -> float:
        return self._summe

    @summe.setter
    def summe(self, summe: float):
        self._summe = summe

class Kapitalerhoehung(_Kapitalmassnahme):
    pass

class Kapitalherabsetzung(_Kapitalmassnahme):
    pass