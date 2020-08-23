#  Copyright (c) 2020 | KingKevin23 (@kingkevin023)

from datetime import datetime

class Index:
    def __init__(self, nummer:int, name:str, highscore:int, punkte:int, gruendung_datum:datetime):
        self._id:int = nummer
        self._name:str = name
        self._highscore:int = highscore
        self._punkte:int = punkte
        self._gruendung_datum:datetime = gruendung_datum

    @property
    def id(self) -> int:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def highscore(self) -> int:
        return self._highscore

    @property
    def punkte(self) -> int:
        return self._punkte

    @property
    def gruendung_datum(self) -> datetime:
        return self._gruendung_datum