#  Copyright (c) 2020 | KingKevin23 (@kingkevin023)

from datetime import datetime

class Zertifikat:
    def __init__(self, betrag:float, typ:str, hebel:float, punkte:int, ablaufdatum:datetime):
        self.betrag:float = betrag
        self.typ:str = typ
        self.hebel:float = hebel
        self.punkte:int = punkte
        self.ablaufdatum:datetime = ablaufdatum

    @property
    def betrag(self) -> float:
        return self._betrag

    @betrag.setter
    def betrag(self, value:float):
        self._betrag = value

    @property
    def typ(self) -> str:
        return self._typ

    @typ.setter
    def typ(self, value:str):
        self._typ = value

    @property
    def hebel(self) -> float:
        return self._hebel

    @hebel.setter
    def hebel(self, value:float):
        self._hebel = value

    @property
    def punkte(self) -> int:
        return self._punkte

    @punkte.setter
    def punkte(self, value:int):
        self._punkte = value

    @property
    def ablaufdatum(self) -> datetime:
        return self._ablaufdatum

    @ablaufdatum.setter
    def ablaufdatum(self, value:datetime):
        self._ablaufdatum = value