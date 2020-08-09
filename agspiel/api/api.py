#  Copyright (c) 2020 | KingKevin23 (@kingkevin023)

from .ag import Ag
from .ceo import Ceo
from .aktie import Aktie, Aktionaer
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
        ceo_data = data.get("ceo")
        ceo = Ceo(name=ceo_data.get("name"), registrierung_datum=datetime.strptime(ceo_data.get("registrierung_datum"), "%Y-%m-%d %H:%M:%S"),
                  gesperrt=ceo_data.get("gesperrt")=="true", userprojekt=ceo_data.get("ist_userprojekt_account")=="true")
        aktien = data.get("aktien")
        anleihen = data.get("anleihen")
        kredite = data.get("kredite")
        zertifikate = data.get("zertifikate")
        orders = data.get("orders")
        return Ag(wkn=int(data.get("wkn")), name=data.get("name"), gruendung=datetime.strptime(data.get("gruendung"), "%Y-%m-%d %H:%M:%S"),
                  aktienanzahl=int(data.get("aktienanzahl")), in_liquidation=data.get("in_liquidation")=="true",
                  kurs=float(data.get("kurs")), brief=float(data.get("brief")), geld=float(data.get("geld")),
                  brief_stueckzahl=int(data.get("brief_stueckzahl")), geld_stueckzahl=int(data.get("geld_stueckzahl")),
                  depotwert=float(data.get("depotwert")), bargeld=float(data.get("bargeld")), highscore=int(data.get("highscore_platz")),
                  highscore_groesse=int(data.get("highscore_platz_groesse")), highscore_newcomer=int(data.get("highscore_platz_newcomer")),
                  highscore_wachstum=int(data.get("highscore_platz_wachstum")), agsx_punkte=int(data.get("agsx_punkte")),
                  in_agsx=data.get("in_agsx")=="true", handelsaktivitaet=int(data.get("handelsaktivitaet")), ceo=ceo,
                  aktien=aktien, anleihen=anleihen, kredite=kredite, zertifikate=zertifikate, orders=orders)

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