#  Copyright (c) 2020 | KingKevin23 (@kingkevin023)

import requests, json, re
from .ag import Ag
from .markt import Markt
from datetime import datetime
from bs4 import BeautifulSoup
from .ceo import Ceo
from .aktie import Aktie
from .anleihe import Anleihe, Kredit
from .zertifikat import Zertifikat
from .order import Order

class Api:
    _api_url = "https://www.ag-spiel.de/api/get/data.php?version=5"

    def __init__(self, phpsessid:str, newest_data:bool=False):
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
        web = requests.get("https://www.ag-spiel.de/index.php?section=profil&aktie={}".format(str(wkn)),
                                                       cookies={"PHPSESSID":self._phpsessid}).content
        return Api._create_ag(api_data=data, web_data=BeautifulSoup(web, "html.parser"))

    def get_markt(self) -> Markt:
        data = self._get_data().get("allgemein")
        web = requests.get("https://www.ag-spiel.de/index.php?section=login").content
        return Api._create_markt(api_data=data, web_data=BeautifulSoup(web, "html.parser"))

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
            return json.loads(requests.get(Api._api_url).content)
        else:
            if self._data is None:
                self._data = json.loads(requests.get(Api._api_url).content)

            return self._data

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

    @staticmethod
    def _create_ag(api_data:dict, web_data:BeautifulSoup) -> Ag:
        """
        Diese Methode erstellt ein Objekt der Klasse AG und befüllt dieses mit den übergebenen Werten.

        :param api_data: Ein Dictionary, welches die Daten aus der API enthält
        :param web_data: Ein BeatifulSoup Objekt, welches die Website der AG enthält
        :return: Ein Objekt der Klasse AG, welches die gewünschten Werte enthält
        """
        ag = Ag()
        ag.wkn = int(api_data.get("wkn"))
        ag.name = api_data.get("name")
        ag.gruendung = datetime.strptime(api_data.get("gruendung"), "%Y-%m-%d %H:%M:%S")
        ag.aktienanzahl = int(api_data.get("aktienanzahl"))
        ag.in_liquidation = api_data.get("in_liquidation") == "true"
        ag.kurs = float(api_data.get("kurs"))
        ag.brief = float(api_data.get("brief"))
        ag.geld = float(api_data.get("geld"))
        ag.brief_stueckzahl = int(api_data.get("brief_stueckzahl"))
        ag.geld_stueckzahl = int(api_data.get("geld_stueckzahl"))
        ag.sw_aktie = float(re.compile("\d*[.]?\d*[,]\d{2}").findall(web_data.find("div", attrs={"id":"sw"}).text)[0]
                            .replace(".", "").replace(",", "."))
        ag.bbw_aktie = float(re.compile("\d*[.]?\d*[,]\d{2}").findall(web_data.find("div", attrs={"id": "bbw"}).text)[0]
                             .replace(".", "").replace(",", "."))
        ag.fp_aktie = float(re.compile("\d*[.]?\d*[,]\d{2}").findall(web_data.find("div", attrs={"id": "fp"}).text)[0]
                            .replace(".", "").replace(",", "."))
        ag.kgv = float(re.compile("\d*[,]\d*").findall(web_data.find("div", attrs={"id":"kgv"}).text)[0].
                       replace(",", "."))
        ag.tagesvolumen = Api._convert_number(web_data.find("div", attrs={"id":"tagesvolumen"}).text)
        ag.depotwert = float(api_data.get("depotwert"))
        ag.bargeld = float(api_data.get("bargeld"))
        ag.highscore = int(api_data.get("highscore_platz"))
        ag.highscore_groesse = int(api_data.get("highscore_platz_groesse"))
        ag.highscore_wachstum = int(api_data.get("highscore_platz_wachstum"))
        ag.highscore_newcomer = int(api_data.get("highscore_platz_newcomer"))
        ag.agsx_punkte = int(api_data.get("agsx_punkte"))
        ag.in_agsx = api_data.get("in_agsx") == "true"
        ag.handelsaktivitaet = int(api_data.get("handelsaktivitaet"))
        ag.ceo = Api._create_ceo(ceo_data=api_data.get("ceo"), web_data=web_data)

        ag.aktien = []
        for i in api_data.get("aktien"):
            temp = Aktie(wkn=int(i.get("wkn")), stueckzahl=int(i.get("stueckzahl")))
            ag.aktien.append(temp)

        ag.anleihen = []
        for i in api_data.get("anleihen"):
            temp = Anleihe(betrag=int(i.get("betrag")), zins=float(i.get("zins")),
                           auszahlung_datum=datetime.strptime(i.get("auszahlung_datum"), "%Y-%m-%d %H:%M:%S"),
                           laufzeit=int(i.get("laufzeit")))
            ag.anleihen.append(temp)

        ag.kredite = []
        for i in api_data.get("kredite"):
            temp = Kredit(betrag=int(i.get("betrag")), zins=float(i.get("zins")),
                          rueckzahlung_datum=datetime.strptime(i.get("rueckzahlung_datum"), "%Y-%m-%d %H:%M:%S"),
                          laufzeit=int(i.get("laufzeit")))
            ag.kredite.append(temp)

        ag.zertifikate = []
        for i in api_data.get("zertifikate"):
            try:
                hebel = float(i.get("hebel"))
            except TypeError:
                hebel = 0
            typ = i.get("typ")
            temp = Zertifikat(betrag=float(i.get("betrag")), typ=typ, hebel=hebel, punkte=int(i.get("punkte")),
                              ablaufdatum=datetime.strptime(i.get("ablauf_datum"), "%Y-%m-%d %H:%M:%S"))
            ag.zertifikate.append(temp)

        ag.orders = []
        for i in api_data.get("orders"):
            temp = Order(typ=i.get("typ"), limit=float(i.get("limit")), stueckzahl=int(i.get("stueckzahl")),
                         orderregel=i.get("orderregel") == "true", systembank=i.get("systembank_order") == "true",
                         datum=datetime.strptime(i.get("datum"), "%Y-%m-%d %H:%M:%S"))
            ag.orders.append(temp)

        table_data = []
        rows = web_data.find('table', attrs={'class': 'normalborder'}).find_all('tr')
        for row in rows:
            cols = row.find_all("td")
            for col in cols:
                inhalt = col.find_all("span")
                try:
                    table_data.append(float(inhalt[0].text.replace(",", ".")))
                except IndexError:
                    pass

        print(table_data)

        offset = int(len(table_data) / 3) - 1 # Die Länge sollte immer glatt durch 3 teilbar sein

        # Fall das len = 0 ist muss nicht beachtet werden, da Werte standardmäßig None
        if len(table_data) >= 3:
            ag.kurs_14d = table_data[0]
            ag.bw_14d = table_data[1 + offset]
            ag.fp_14d = table_data[2 + offset * 2]
        if len(table_data) >= 6:
            ag.kurs_30d = table_data[1]
            ag.bw_30d = table_data[2 + offset]
            ag.fp_30d = table_data[3 + offset * 2]
        if len(table_data) >= 9:
            ag.kurs_60d = table_data[2]
            ag.bw_60d = table_data[3 + offset]
            ag.fp_60d = table_data[4 + offset * 2]
        if len(table_data) >= 12:
            ag.kurs_90d = table_data[3]
            ag.bw_90d = table_data[4 + offset]
            ag.fp_90d = table_data[5 + offset * 2]


        table_data = {}
        rows = web_data.find('table', attrs={'class': 'padding5'}).find_all('tr')
        for row in rows:
            cols = row.find_all("td")
            table_data[cols[0].text] = cols[1].text

        ag.dividende = float(re.compile("(0\.?\d{0,2})%").findall(table_data.get("Dividende"))[0])
        ag.max_zertis = int(re.compile("(\d{1,2})%").findall(table_data.get("Max. Zertifikatevol."))[0])
        ag.tages_hoch = float(re.compile("\d*\.?\d*,?\d*").findall(table_data.get("Tageshoch"))[0].replace(".", "").
                              replace(",", "."))
        ag.tages_tief = float(re.compile("\d*\.?\d*,?\d*").findall(table_data.get("Tagestief"))[0].replace(".", "").
                              replace(",", "."))

        return ag

    @staticmethod
    def _create_ceo(ceo_data:dict, web_data:BeautifulSoup) -> Ceo:
        """
        Diese Methode erstellt ein Objekt der Klasse CEO und befüllt dieses mit den übergebenen Werten.

        :param ceo_data: Ein Dictionary, welches die Daten aus der API über den CEO enthält
        :param web_data: Ein BeatifulSoup Objekt, welches die Website der AG des CEO enthält
        :return: Ein Objekt der Klasse CEO, welches die gewünschten Werte enthält
        """
        name = ceo_data.get("name")
        try:
            index = re.compile("Spielerindex:.(.*)").findall(web_data.find("img", attrs={"width":"150"}).attrs.get("title"))[0]
        except AttributeError: # Für den Fall das Spieler in keinem Index ist
            index = None
        registrierung_datum = datetime.strptime(ceo_data.get("registrierung_datum"), "%Y-%m-%d %H:%M:%S")
        gesperrt = ceo_data.get("gesperrt")=="true"
        userprojekt = ceo_data.get("ist_userprojekt_account")=="true"
        return Ceo(name=name, index=index, registrierung_datum=registrierung_datum, gesperrt=gesperrt, userprojekt=userprojekt)

    @staticmethod
    def _convert_number(number:str) -> float:
        """
        Diese Methode wandelt Zahlen in der Form "5,6 Mio." in Gleitkommazahlen um.

        :param number: Die umzuwandelnde Zahl
        :return: Die umgewandelte Gleitkommazahl
        """
        ergebnis = float(re.compile("\d+[,]?\d*").findall(number)[0].replace(",", "."))
        multiplier = re.compile("\d*[,]?\d*.(:Mrd\.|Mio\.|Tsd\.)").findall(number)
        if multiplier:
            multiplier = multiplier[0]
            if multiplier == "Mrd.":
                ergebnis *= 1000000000
            elif multiplier == "Mio.":
                ergebnis *= 1000000
            elif multiplier == "Tsd.":
                ergebnis *= 1000
            else:
                raise ValueError()

        return ergebnis