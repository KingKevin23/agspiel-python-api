#  Copyright (c) 2020 | KingKevin23 (@kingkevin023)

import requests, json
from .ag import Ag
from .markt import Markt
from datetime import datetime
from bs4 import BeautifulSoup
from .data import Data

class AgNotFoundError(Exception): pass

class Api:
    _api_url = "https://www.ag-spiel.de/api/get/data.php?version=5"

    def __init__(self, phpsessid:str="", premium:bool=True):
        self._phpsessid = phpsessid
        self.premium = premium
        self._api_data = Data(update=lambda: json.loads(requests.get(Api._api_url).content))

    def get_ag(self, wkn:int) -> Ag:
        """
        Diese Methode gibt ein Objekt der Klasse Ag mit der übergebenen WKN aus.

        :param wkn: Die WKN der gewünschten Ag
        :return: Ein Objekt der Klasse Ag
        """
        if str(wkn) in self._api_data().get("ags"):
            web_data = Data(
                update=lambda: BeautifulSoup(requests.get("https://www.ag-spiel.de/index.php?section=profil&aktie={}"
                                                          .format(str(wkn)), cookies={"PHPSESSID": self._phpsessid})
                                             .content, "html.parser"))
            return Ag(wkn=wkn, api_data=self._api_data, web_data=web_data)
        else:
            raise AgNotFoundError("Die AG mit der WKN " + str(wkn) + " wurde nicht gefunden.")

    def get_all_ags(self) -> list:
        """
        Diese Methode gibt eine Liste mit allen Ag-Objekten aus, die es im AG-Spiel gibt.

        :return: Die Liste aller AGs
        """
        ergebnis = []
        for i in self._api_data().get("ags"):
            ergebnis.append(self.get_ag(int(i)))

        return ergebnis

    def get_markt(self) -> Markt:
        web_data = Data(update=lambda: BeautifulSoup(requests.get("https://www.ag-spiel.de/index.php?section=statistiken",
                                                                  cookies={"PHPSESSID": self._phpsessid}).content, "html.parser"))
        return Markt(api_data=self._api_data, web_data=web_data)

    @property
    def api_version(self) -> int:
        return int(self._api_data().get("api_version"))

    @property
    def daten_datum(self) -> datetime:
        return datetime.strptime(self._api_data().get("daten_datum"), "%Y-%m-%d %H:%M:%S")