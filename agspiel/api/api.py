#  Copyright (c) 2020 | KingKevin23 (@kingkevin023)

from .ag import Ag
from .markt import Markt
from datetime import datetime
import urllib.request, json

class Api:
    _api_url = "https://www.ag-spiel.de/api/get/data.php?version=5"

    def __init__(self, phpsessid:str, newest_data:bool=True):
        self._phpsessid = phpsessid
        self._newest_data = newest_data
        self._data = None

    def get_ag(self, wkn:int) -> Ag:
        """
        Diese Methode gibt ein Objekt der Klasse Ag mit der übergebenen WKN aus.

        :param wkn: Die WKN der gewünschten Ag
        :return: Ein Objekt der Klasse Ag
        """
        data = self._get_data().get("ags").get(str(wkn))
        return Ag(api_data=data, web_data="")

    def get_markt(self) -> Markt:
        data = self._get_data().get("allgemein")
        return Markt(ags=data.get("ags"), orders_24=data.get("24_stunden_orders"), volumen_24=data.get("24_stunden_ordervolumen"))

    @property
    def api_version(self) -> int:
        return int(self._get_data().get("api_version"))

    @property
    def daten_datum(self) -> datetime:
        return datetime.strptime(self._get_data().get("daten_datum"), "%Y-%m-%d %H:%M:%S")

    def _get_data(self) -> dict:
        """
        Diese Methode holt sich die aktuellen Daten aus der AGS-API.

        :return: Ein Dictionary mit den API-Daten
        """
        if self._newest_data:
            with urllib.request.urlopen(Api._api_url) as url:
                return json.loads(url.read())
        else:
            if self._data is None:
                with urllib.request.urlopen(Api._api_url) as url:
                    self._data = json.loads(url.read())
                    return self._data
            else:
                return self._data