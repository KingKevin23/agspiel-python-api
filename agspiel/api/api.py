#  Copyright (c) 2020 | KingKevin23 (@kingkevin023)

import requests, json, re
from .ag import Ag
from .markt import Markt
from datetime import datetime
from bs4 import BeautifulSoup
from .data import Data

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
        if str(wkn) in self._api_data:
            web_data = Data(
                update=lambda: BeautifulSoup(requests.get("https://www.ag-spiel.de/index.php?section=profil&aktie={}"
                                                          .format(str(wkn)), cookies={"PHPSESSID": self._phpsessid})
                                             .content, "html.parser"))
            return Ag(wkn=wkn, api_data=self._api_data, web_data=web_data)
        else:
            raise AgNotFoundError("Die AG mit der WKN " + str(wkn) + " wurde nicht gefunden.")

    def get_all_ags(self) -> list:
        ergebnis = []
        for i in self._api_data().get("ags"):
            print(i)
            ergebnis.append(self.get_ag(int(i)))

        return ergebnis

    def get_markt(self) -> Markt:
        data = self._api_data().get("allgemein")
        web = requests.get("https://www.ag-spiel.de/index.php?section=login").content
        return Api._create_markt(api_data=data, web_data=BeautifulSoup(web, "html.parser"))

    @property
    def api_version(self) -> int:
        return int(self._api_data().get("api_version"))

    @property
    def daten_datum(self) -> datetime:
        return datetime.strptime(self._api_data().get("daten_datum"), "%Y-%m-%d %H:%M:%S")

    @staticmethod
    def _create_markt(api_data:dict, web_data:BeautifulSoup) -> Markt:
        markt = Markt()
        markt.ags = int(api_data.get("ags"))
        markt.orders_24 = int(api_data.get("24_stunden_orders"))
        markt.volumen_24 = float(api_data.get("24_stunden_ordervolumen"))

        table_data = {}
        rows = web_data.find('table', attrs={'class': 'menu2'}).find_all('tr')
        for row in rows:
            cols = row.find_all("td")
            try:
                table_data[cols[0].text] = cols[1].text
            except IndexError:
                pass

        markt.agsx_punkte = int(table_data.get("Punktestand").replace(".", ""))
        markt.agsx_aenderung = int(table_data.get("Änderung"))
        markt.put_hebel = float(re.compile("(\d\.?\d*)\s/\s\d\.?\d*").findall(table_data.get("Put / Call"))[0])
        markt.call_hebel = float(re.compile("\d\.?\d*\s/\s(\d\.?\d*)").findall(table_data.get("Put / Call"))[0])
        markt.anleihenzins = float(re.compile("(\d\.?\d*)%").findall(table_data.get("Anleihezins"))[0])

        return markt

class AgNotFoundError(Exception): pass