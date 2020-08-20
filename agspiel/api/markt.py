#  Copyright (c) 2020 | KingKevin23 (@kingkevin023)

import re
from .data import Data

class Markt:
    def __init__(self, api_data:Data, web_data:Data):
        self._api_data = api_data
        self._web_data = web_data
        self._markt_data = lambda: self._api_data().get("allgemein")

    @property
    def ags(self) -> int:
        return int(self._markt_data().get("ags"))

    @property
    def orders_24(self) -> int:
        return int(self._markt_data().get("24_stunden_orders"))

    @property
    def volumen_24(self) -> float:
        return float(self._markt_data().get("24_stunden_ordervolumen"))

    @property
    def agsx_punkte(self) -> int:
        table_data = {}
        rows = self._web_data().find('table', attrs={'class': 'menu2'}).find_all('tr')
        for row in rows:
            cols = row.find_all("td")
            try:
                table_data[cols[0].text] = cols[1].text
            except IndexError:
                pass

        return int(table_data.get("Punktestand").replace(".", ""))

    @property
    def agsx_aenderung(self) -> int:
        table_data = {}
        rows = self._web_data().find('table', attrs={'class': 'menu2'}).find_all('tr')
        for row in rows:
            cols = row.find_all("td")
            try:
                table_data[cols[0].text] = cols[1].text
            except IndexError:
                pass

        return int(table_data.get("Änderung"))

    @property
    def put_hebel(self) -> float:
        table_data = {}
        rows = self._web_data().find('table', attrs={'class': 'menu2'}).find_all('tr')
        for row in rows:
            cols = row.find_all("td")
            try:
                table_data[cols[0].text] = cols[1].text
            except IndexError:
                pass

        return float(re.compile("(\d\.?\d*)\s/\s\d\.?\d*").findall(table_data.get("Put / Call"))[0])

    @property
    def call_hebel(self) -> float:
        table_data = {}
        rows = self._web_data().find('table', attrs={'class': 'menu2'}).find_all('tr')
        for row in rows:
            cols = row.find_all("td")
            try:
                table_data[cols[0].text] = cols[1].text
            except IndexError:
                pass

        return float(re.compile("\d\.?\d*\s/\s(\d\.?\d*)").findall(table_data.get("Put / Call"))[0])

    @property
    def anleihenzins(self) -> float:
        table_data = {}
        rows = self._web_data().find('table', attrs={'class': 'menu2'}).find_all('tr')
        for row in rows:
            cols = row.find_all("td")
            try:
                table_data[cols[0].text] = cols[1].text
            except IndexError:
                pass

        return float(re.compile("(\d\.?\d*)%").findall(table_data.get("Anleihezins"))[0])