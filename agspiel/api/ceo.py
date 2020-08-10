#  Copyright (c) 2020 | KingKevin23 (@kingkevin023)

from datetime import datetime

class Ceo:
    def __init__(self, name:str, index:str, registrierung_datum:datetime, gesperrt:bool, userprojekt:bool):
        self.name:str = name
        self.index:str = index
        self.registrierung_datum:datetime = registrierung_datum
        self.gesperrt:bool = gesperrt
        self.userprojekt:bool = userprojekt

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value:str):
        self._name = value

    @property
    def index(self) -> str:
        return self._index

    @index.setter
    def index(self, value: str):
        self._index = value

    @property
    def registrierung_datum(self) -> datetime:
        return self._registrierung_datum

    @registrierung_datum.setter
    def registrierung_datum(self, value:datetime):
        self._registrierung_datum = value

    @property
    def gesperrt(self) -> bool:
        return self._gesperrt

    @gesperrt.setter
    def gesperrt(self, value:bool):
        self._gesperrt = value

    @property
    def userprojekt(self) -> bool:
        return self._userprojekt

    @userprojekt.setter
    def userprojekt(self, value:bool):
        self._userprojekt = value