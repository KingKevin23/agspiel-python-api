# Einführung in die API

Der Zugriff auf die API erfolgt über die [agspiel.api.Api](../../agspiel/api/api.py) Klasse. Bevor man auf diese jedoch zugreifen kann, muss die API installieren und in sein Projekt importieren.

#### Installation

Die Installation erfolgt über die Kommandozeile, vorausgesetzt wird Python 3.8. Die Installation erfolgt über einen einfachen PIP-Befehl:

```
pip install agspiel-python-api
```

Alle anderen erforderlichen Python-Module werden automatisch installiert.

#### In Projekt importieren

Nachdem die Installation erfolgreich abgeschlossen wurde, kann man die API in sein Projekt einbinden. Dies erfolgt über einen einfachen Import-Befehl:

```python
import agspiel
```

#### API erzeugen

Um die API nun nutzen zu können, muss man ein Objekt der Klasse [agspiel.api.Api](../../agspiel/api/api.py) erzeugen. Dies geht so:

```python
api = agspiel.api.Api("Deine PHPSESSID")
```

Die API nimmt hierbei über den Parameter `phpsessid` die PHPSESSID als String entgegen. Dieser wird genutzt um sich gegenüber dem AGS-Server zu verifizieren. Dieses kann man über die Cookie-Ansicht seines Browsers oder über eine [Hilfsfunktion](hilfsfunktionen.md) erhalten.&#x20;

#### API nutzen

Wenn man nun im vorherigen Schritt ein API-Objekt erzeugt hat, kann man nun die API nutzen. Folgende Attribute können abgefragt werden:

* `api_version` -> Version der API von Rady (`int`)
* `daten_datum` -> Stand der Daten aus Radys API (`datetime`)

Die wichtigsten Abfragen sind für die meisten jedoch wahrscheinlich die `get_markt()` und `get_ag(wkn:int)` Methode. `get_markt()` liefert ein Objekt der Klasse [Markt](../classes/markt.md), während `get_ag(wkn:int)` eine WKN als `int` übergeben bekommt und daraufhin ein passendes Objekt der Klasse [Ag](../classes/ag.md) ausgibt. Außerdem kann man mit `get_all_ags()` eine Liste mit allen AGs anfordern. Es ist ebenfalls möglich an historische Daten zu gelangen, hierzu gibt es Infos im Abschnitt [Historische Daten](historische-daten.md).

#### Hinweise zur Aktualität der Daten

Die Daten in der Python-API sind maximal fünf Minuten alt. Genauer: Bei jedem fünf Minuten Tick (auch zur vollen Stunde) aktualisieren sich die Daten automatisch. Dies geschieht aber erst, wenn aktiv darauf zugegriffen wird.

Beispiel: Um 14:41 Uhr fragt man von der API den SW/Aktie von AG X ab. Diese Daten haben dann den Stand von 14:41 Uhr. Um 14:45 Uhr würden die Daten aktualisiert. Da man aber erst um 14:48 Uhr erneut auf die Daten von AG X zugreift, haben diese den Stand von 14:48 Uhr.
