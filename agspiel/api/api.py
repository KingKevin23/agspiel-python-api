#  Copyright (c) 2020 | KingKevin23 (@kingkevin023)

from .ag import Ag
import urllib.request, json, datetime

class Api:
    def __init__(self, phpsessid:str, newest_data:bool=True):
        self._phpsessid = phpsessid
        self._newest_data = newest_data
        self._data = None

    def get_ag(self, wkn:int) -> object:
        """
        Diese Methode gibt ein Objekt der Klasse Ag mit der übergebenen WKN aus.

        :param wkn: Die WKN der gewünschten Ag
        :return: Ein Objekt der Klasse Ag
        """
        data = self._get_data()
        test = data.get("ags").get(str(wkn))
        return Ag(data.get("ags").get(str(wkn)))

    def _get_data(self) -> dict:
        """
        Diese Methode holt sich die aktuellen Daten aus der AGS-API.

        :return: Ein Dictionary mit den API-Daten
        """
        if self._newest_data:
            with urllib.request.urlopen("https://www.ag-spiel.de/api/get/data.php") as url:
                return json.loads(url.read())
        else:
            if self._data is None:
                with urllib.request.urlopen("https://www.ag-spiel.de/api/get/data.php") as url:
                    self._data = json.loads(url.read())
                    return self._data
            else:
                return self._data