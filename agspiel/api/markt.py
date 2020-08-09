#  Copyright (c) 2020 | KingKevin23 (@kingkevin023)

class Markt:
    def __init__(self, ags:int, orders_24:int, volumen_24:float):
        self.ags:int = ags
        self.orders_24:int = orders_24
        self.volumen_24:float = volumen_24

    @property
    def ags(self) -> int:
        return self._ags

    @ags.setter
    def ags(self, value:int):
        self._ags = value

    @property
    def orders_24(self) -> int:
        return self._orders_24

    @orders_24.setter
    def orders_24(self, value:int):
        self._orders_24 = value

    @property
    def volumen_24(self) -> float:
        return self._volumen_24

    @volumen_24.setter
    def volumen_24(self, value:float):
        self._volumen_24 = value