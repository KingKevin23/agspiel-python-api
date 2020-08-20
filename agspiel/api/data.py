#  Copyright (c) 2020 | KingKevin23 (@kingkevin023)

from datetime import datetime

class Data:
    def __init__(self, update, data=None):
        self.data = data
        self.update = update # type(update) -> function
        self.timestamp = datetime.now()

    def _update_data(self):
        self.data = self.update()

    @property
    def data(self):
        if self._data is None:
            self._update_data()
        else:
            now = datetime.now()
            now = (now.minute + (now.hour * 60) + (now.day * 24 * 60)) % 5
            compare = (self.timestamp.minute + (self.timestamp.hour * 60) + (self.timestamp.day * 24 * 60)) % 5
            if now > compare:
                self._update_data()

        return self._data

    @data.setter
    def data(self, value):
        self._data = value
        self.timestamp = datetime.now()

    @property
    def update(self):
        return self._update

    @update.setter
    def update(self, value):
        self._update = value

    @property
    def timestamp(self) -> datetime:
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value:datetime):
        self._timestamp = value

    def __call__(self, *args, **kwargs):
        return self.data