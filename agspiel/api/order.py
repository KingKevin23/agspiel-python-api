#  Copyright (c) 2020 | KingKevin23 (@kingkevin023)

from datetime import datetime

class Order:
    def __init__(self, typ:str, limit:float, stueckzahl:int, orderregel:bool, systembank:bool, datum:datetime):
        self.typ:str = typ
        self.limit:float = limit
        self.stueckzahl:int = stueckzahl
        self.orderregel:bool = orderregel
        self.systembank:bool = systembank
        self.datum:datetime = datum

    @property
    def typ(self) -> str:
        return self._typ

    @typ.setter
    def typ(self, value:str):
        self._typ = value

    @property
    def limit(self) -> float:
        return self._limit

    @limit.setter
    def limit(self, value:float):
        self._limit = value

    @property
    def stueckzahl(self) -> int:
        return self._stueckzahl

    @stueckzahl.setter
    def stueckzahl(self, value:int):
        self._stueckzahl = value

    @property
    def orderregel(self) -> bool:
        return self._orderregel

    @orderregel.setter
    def orderregel(self, value:bool):
        self._orderregel = value

    @property
    def systembank(self) -> bool:
        return self._systembank

    @systembank.setter
    def systembank(self, value:bool):
        self._systembank = value

    @property
    def datum(self) -> datetime:
        return self._datum

    @datum.setter
    def datum(self, value:datetime):
        self._datum = value