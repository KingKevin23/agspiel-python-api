#  Copyright (c) 2021 | KingKevin23 (@kingkevin023)

from datetime import datetime

from .index import Index


class Ceo:
    def __init__(self, name: str, index: Index, registrierung_datum: datetime, gesperrt: bool, userprojekt: bool):
        self._name: str = name
        self._index: Index = index
        self._registrierung_datum: datetime = registrierung_datum
        self._gesperrt: bool = gesperrt
        self._userprojekt: bool = userprojekt

    @property
    def name(self) -> str:
        return self._name

    @property
    def index(self) -> Index:
        return self._index

    @property
    def registrierung_datum(self) -> datetime:
        return self._registrierung_datum

    @property
    def gesperrt(self) -> bool:
        return self._gesperrt

    @property
    def userprojekt(self) -> bool:
        return self._userprojekt