#  Copyright (c) 2021 | KingKevin23 (@kingkevin023)

from datetime import datetime, date

class HistorischeAg:

    # Currently not included stats:
    # UserID, IndexID, Premiumstatus, Übernahmeschutz, AGSXDurchschnittsplatzierung, Wachstumsdurchschnittsplatz

    def __init__(self, wkn:int, datum:date, api_data:dict):
        self._wkn:int = wkn
        self._datum:date = datum
        self._api_data:dict = api_data

    @property
    def wkn(self) -> int:
        return self._wkn

    @property
    def datum(self) -> date:
        return self._datum

    @property
    def name(self) -> str:
        return self._api_data.get("AGName")

    # @property
    # def logo(self) -> str:
    #     pass

    @property
    def gruendung(self) -> datetime:
        return datetime.strptime(self._api_data.get("Gruendungsdatum"), "%Y-%m-%d")

    @property
    def aktienanzahl(self) -> int:
        return self._api_data.get("Aktienanzahl")

#   @property
#   def in_liquidation(self) -> bool:
#       pass

    @property
    def kurs(self) -> float:
        return self._api_data.get("Kurs_Wert")

    @property
    def brief(self) -> float:
        return self._api_data.get("Briefkurs_Wert")

    @property
    def geld(self) -> float:
        return self._api_data.get("Geldkurs_Wert")

    @property
    def brief_stueckzahl(self) -> int:
        return int(self._api_data.get("Briefvolumen"))

    @property
    def geld_stueckzahl(self) -> int:
        return int(self._api_data.get("Geldvolumen"))

    @property
    def sw_aktie(self) -> float:
        return self._api_data.get("SW_Wert")

    @property
    def bbw_aktie(self) -> float:
        return self._api_data.get("BBW_Wert")

    @property
    def fp_aktie(self) -> float:
        return self._api_data.get("FP_Wert")

    @property
    def bw_aktie(self) -> float:
        return self._api_data.get("BW_Wert")

#   @property
#   def kgv(self) -> float:
#       pass

    @property
    def spread(self) -> float:
        if self.geld == 0 or self.brief == 0:
            return 0
        else:
            return 1 - (self.geld / self.brief)

    @property
    def alter(self) -> int:
        return (datetime.now() - self.gruendung).days

#   @property
#   def tagesvolumen(self) -> float:
#       pass

    @property
    def boersenwert(self) -> float:
        return self.kurs * self.aktienanzahl

    @property
    def buchwert(self) -> float:
        return self.bargeld + self.depotwert

    @property
    def depotwert(self) -> float:
        return self._api_data.get("Aktienbuchwert_Wert") + self._api_data.get("Anleihen_Wert") + self._api_data.get("Zertifikate_Wert")

    @property
    def bargeld(self) -> float:
        return self._api_data.get("Cash_Wert")

    @property
    def highscore(self) -> int:
        return self._api_data.get("Platz")

    @property
    def highscore_groesse(self) -> int:
        return self._api_data.get("Groessenplatz")

    @property
    def highscore_wachstum(self) -> int:
        return self._api_data.get("Wachstumsplatz")

#   @property
#   def highscore_newcomer(self) -> int:
#       pass

    @property
    def agsx_punkte(self) -> int:
        return self._api_data.get("AGSXPunkte")

    @property
    def in_agsx(self) -> bool:
        return self.highscore_wachstum <= 10 or self.highscore_groesse <= 10

    @property
    def handelsaktivitaet(self) -> int:
        return int(self._api_data.get("Aktivitaet"))

#   @property
#   def ceo(self):
#       pass
#
#   @property
#   def aktien(self):
#       pass
#
#   @property
#   def anleihen(self): #todo This could be possible via the historic bond drawer and historic bond zins
#       pass
#
#   @property
#   def kredite(self):
#       pass
#
#   @property
#   def zertifikate(self):
#       pass
#
#   @property
#   def orders(self):
#       pass
#
#   @property
#   def aktionaere(self):
#       pass
#
#   @property
#   def kes(self):
#       pass
#
#   @property
#   def khs(self):
#       pass
#
#   @property
#   def dividende(self) -> float:
#       pass
#
#   @property
#   def max_zertis(self) -> int:
#       pass
#
#   @property
#   def uebernahmeschutz(self) -> bool:
#       pass
#
#   @property
#   def tages_hoch(self) -> float:
#       pass
#
#   @property
#   def tages_tief(self) -> float:
#       pass
#
#   @property
#   def kurs_14d(self) -> float:
#       pass
#
#   @property
#   def kurs_30d(self) -> float:
#       pass
#
#   @property
#   def kurs_60d(self) -> float:
#       pass
#
#   @property
#   def kurs_90d(self) -> float:
#       pass
#
#   @property
#   def bw_14d(self) -> float:
#       pass
#
#   @property
#   def bw_30d(self) -> float:
#       pass
#
#   @property
#   def bw_60d(self) -> float:
#       pass
#
#   @property
#   def bw_90d(self) -> float:
#       pass
#
#   @property
#   def fp_14d(self) -> float:
#       pass
#
#   @property
#   def fp_30d(self) -> float:
#       pass
#
#   @property
#   def fp_60d(self) -> float:
#       pass
#
#   @property
#   def fp_90d(self) -> float:
#       pass