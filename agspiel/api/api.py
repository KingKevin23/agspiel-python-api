#  Copyright (c) 2021 | KingKevin23 (@kingkevin023)

from datetime import datetime, date, timedelta

import json
from typing import Union

from requests import get, post
from bs4 import BeautifulSoup

from .ag import Ag
from .data import Data
from .markt import Markt
from .historic_ag import HistorischeAg


class AgNotFoundError(Exception): pass


class Api:
    _api_url = "https://www.ag-spiel.de/api/get/data.php?version=5"
    _historic_api_url = "http://api.agscio.de:8080/apiserver/api.rsc"

    def __init__(self, phpsessid: str = "", api_key:str="0t7B1d3c0G5k9i3O8q1j", premium: bool = True):
        self._phpsessid = phpsessid
        self._api_key = api_key
        self.premium = premium
        self._api_data = Data(update=lambda: json.loads(get(Api._api_url).content))

    @staticmethod
    def from_user_credentials(email: str, password: str, premium: bool = True) -> "Api":
        """
        Diese Methode erstellt ein Objekt der Klasse Api mit den übergebenen Nutzerdaten und holt sich die PHPSESSID
        automatisch.

        :param email: Die Email des Nutzers
        :param password: Das Passwort des Nutzers
        :param premium: Ob der Nutzer Premium hat
        :return: Ein Objekt der Klasse Api
        """
        login_url = "https://www.ag-spiel.de/index.php?section=login"
        login_data = {
            'email': email,
            'userpass': password,
            'permanent': '1',
            'login': 'Einloggen',
        }
        response = post(login_url, data=login_data)

        if "Einloggen" in response.text:
            raise Exception("Login failed.")

        php_session_id = response.cookies.get('PHPSESSID')

        return Api(phpsessid=php_session_id, premium=premium)

    def get_ag(self, wkn: int, datum:date=None) -> Union[Ag, HistorischeAg]:
        """
        Diese Methode gibt ein Objekt der Klasse Ag mit der übergebenen WKN aus.

        :param wkn: Die WKN der gewünschten Ag
        :param datum: Das Datum von welchem die Ag-Daten stammen sollen
        :return: Ein Objekt der Klasse Ag
        """
        today = date.today()
        if datum is None or datum == today:
            if str(wkn) in self._api_data().get("ags"):
                web_data = Data(
                    update=lambda: BeautifulSoup(
                        get("https://www.ag-spiel.de/index.php?section=profil&aktie={}"
                                     .format(str(wkn)), cookies={"PHPSESSID": self._phpsessid})
                        .content, "html.parser"))
                chronik_data = Data(
                    update=lambda: BeautifulSoup(get("https://www.ag-spiel.de/index.php?section=chronik&wkn={}"
                                                              .format(str(wkn)), cookies={"PHPSESSID": self._phpsessid})
                                                 .content, "html.parser"))
                return Ag(wkn=wkn, api_data=self._api_data, web_data=web_data, chronik_data=chronik_data)
            else:
                raise AgNotFoundError("Die AG mit der WKN " + str(wkn) + " wurde nicht gefunden.")
        elif datum > today:
            raise ValueError("Das Datum liegt in der Zukunft!")
        else:
            link = Api._historic_api_url + f"/Profile_Prem(WKN={wkn}, Datum={datum + timedelta(1)})"
            api_data = get(link, params={"@authtoken": self._api_key}).text
            if api_data == "":
                raise AgNotFoundError("Die AG mit der WKN " + str(wkn) + " wurde zum angegebenen Zeitpunkt nicht gefunden.")
            else:
                return HistorischeAg(wkn, datum, json.loads(api_data))

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
        web_data = Data(
            update=lambda: BeautifulSoup(get("https://www.ag-spiel.de/index.php?section=statistiken",
                                                      cookies={"PHPSESSID": self._phpsessid}).content, "html.parser"))
        return Markt(api_data=self._api_data, web_data=web_data)

    @property
    def api_version(self) -> int:
        return int(self._api_data().get("api_version"))

    @property
    def daten_datum(self) -> datetime:
        return datetime.strptime(self._api_data().get("daten_datum"), "%Y-%m-%d %H:%M:%S")