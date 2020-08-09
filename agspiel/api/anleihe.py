#  Copyright (c) 2020 | KingKevin23 (@kingkevin023)

from datetime import datetime

class _Superclass:
    def __init__(self, betrag:int, zins:float, laufzeit:int):
        self.betrag:int = betrag
        self.zins:float = zins
        self.laufzeit:int = laufzeit

    @property
    def betrag(self) -> int:
        return self._betrag

    @betrag.setter
    def betrag(self, value: int):
        self._betrag = value

    @property
    def zins(self) -> float:
        return self._zins

    @zins.setter
    def zins(self, value: float):
        self._zins = value

    @property
    def laufzeit(self) -> int:
        return self._laufzeit

    @laufzeit.setter
    def laufzeit(self, value: int):
        self._laufzeit = value

class Anleihe(_Superclass):
    def __init__(self, betrag:int, zins:float, auszahlung_datum:datetime, laufzeit:int):
        super().__init__(betrag, zins, laufzeit)
        self.auszahlung_datum:datetime = auszahlung_datum

    @property
    def auszahlung_datum(self) -> datetime:
        return self._auszahlung_datum

    @auszahlung_datum.setter
    def auszahlung_datum(self, value:datetime):
        self._auszahlung_datum = value

class Kredit(_Superclass):
    def __init__(self, betrag:int, zins:float, rueckzahlung_datum:datetime, laufzeit:int):
        super().__init__(betrag, zins, laufzeit)
        self.rueckzahlung_datum:datetime = rueckzahlung_datum

    @property
    def rueckzahlung_datum(self) -> datetime:
        return self._rueckzahlung_datum

    @rueckzahlung_datum.setter
    def rueckzahlung_datum(self, value:datetime):
        self._rueckzahlung_datum = value