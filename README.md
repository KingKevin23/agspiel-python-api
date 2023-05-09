# AG-Spiel API für Python [![Python 3.8](https://img.shields.io/badge/python-3.8-green.svg)](https://www.python.org/downloads/release/python-380/) [![GitHub](https://img.shields.io/github/license/KingKevin23/agspiel-python-api)](https://github.com/KingKevin23/agspiel-python-api/blob/master/LICENSE)

Die ultimative Python API für das [AG-Spiel](http://www.ag-spiel.de/?bonus=83275). Made by KingKevin23. (Aktuell benötigt man einen Premiumaccount um die API fehlerfrei zu benutzen. Bei entsprechender Nachfrage kann ich dies in zukünftigen Versionen beheben)

## Inhaltsverzeichnis

* [Features](#features)
* [Installation](#installation) 
* [Beispiele](#beispiele) 
* [Hinweise](#hinweise)

### Features:

* AG Kennzahlen ausgeben
* Marktdaten ausgeben

### Installation:

`pip install agspiel-python-api`

### Beispiele:

AG-Namen und CEO-Namen ausgeben lassen:

```python
import agspiel

api = agspiel.api.Api("DEINE PHPSESSID")
ag = api.get_ag(175353)

print(ag.name)
print(ag.ceo.name)

> King Kompany
> KingKevin23
```

Weitere Beispiele und Hilfestellungen findest du in der [Dokumentation](https://agspiel-python-api.gitbook.io/documentation/).

### Hinweise:

Diese API oder dieses Projekt stehen in keinerlei Verbindung mit dem Betreiber des Spiels, sondern stellen ein
unabhängiges Userprojekt dar. Desweiten müssen bei allen Projekten, die durch diese API ermöglicht werden oder in denen
diese API eingesetzt wird, die [offiziellen Regeln](https://www.ag-spiel.de/index.php?section=regeln) des AG-Spiels 
beachtet werden. Hierzu zählt insbesondere §5, der im folgenden nochmals zitiert wird:

> Das Benutzen von Programmen/Bots, die einen Spielvorteil ermöglichen, Funktionen bieten die sich mit Premiumfeatures 
> überschneiden oder hohe Serverbelastungen erzeugen (z.B. Parsen der Seite mit mehr als einem Aufruf pro Sekunde), 
> ist verboten. Die Bewerbung/Verbreitung von Browserplugins oder anderer clientseitiger Software zur 
> Erweiterung/Veränderung der Webseite ist verboten.

Bei Fragen zur Legalität des persönlichen Projektes mit dieser API, sollte man sich im Zweifel an die Börsenaufsicht des
AGS wenden ([Hier](https://www.ag-spiel.de/index.php?section=support)).
