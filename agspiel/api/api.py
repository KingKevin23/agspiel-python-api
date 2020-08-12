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
            return json.loads(requests.get(Api._api_url).content)
        else:
            if self._data is None:
                self._data = json.loads(requests.get(Api._api_url).content)

            return self._data

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
        ag.kurs_14d = float(re.compile("[-]?\d*[.]?\d*[,]\d*").findall(web_data.find("div", attrs={"id": "kurs14d"}).
                                                                       text)[0].replace(".", "").replace(",", "."))
        ag.kgv = float(re.compile("\d*[,]\d*").findall(web_data.find("div", attrs={"id":"kgv"}).text)[0].
                       replace(",", "."))
        ag.spread = 1 - (ag.geld / ag.brief)
        ag.alter = (datetime.now() - ag.gruendung).days
        ag.depotwert = float(api_data.get("depotwert"))
        ag.bargeld = float(api_data.get("bargeld"))
        ag.buchwert = ag.depotwert + ag.bargeld
        ag.bw_aktie = round(ag.buchwert / ag.aktienanzahl, 2)
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
            temp = Zertifikat(betrag=float(i.get("betrag")), typ=i.get("typ"),
                              hebel=float(i.get("hebel")), punkte=int(i.get("punkte")),
                              ablaufdatum=datetime.strptime(i.get("ablauf_datum"), "%Y-%m-%d %H:%M:%S"))
            ag.zertifikate.append(temp)

        ag.orders = []
        for i in api_data.get("orders"):
            temp = Order(typ=i.get("typ"), limit=float(i.get("limit")), stueckzahl=int(i.get("stueckzahl")),
                         orderregel=i.get("orderregel") == "true", systembank=i.get("systembank_order") == "true",
                         datum=datetime.strptime(i.get("datum"), "%Y-%m-%d %H:%M:%S"))
            ag.orders.append(temp)

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
        index = re.compile("Spielerindex:.(.*)").findall(web_data.find("img", attrs={"width":"150"}).attrs.get("title"))[0]
        registrierung_datum = datetime.strptime(ceo_data.get("registrierung_datum"), "%Y-%m-%d %H:%M:%S")
        gesperrt = ceo_data.get("gesperrt")=="true"
        userprojekt = ceo_data.get("ist_userprojekt_account")=="true"
        return Ceo(name=name, index=index, registrierung_datum=registrierung_datum, gesperrt=gesperrt, userprojekt=userprojekt)