# Historische Daten

Für diesen Abschnitt wird die [Einführung in die API](einfuehrung-in-die-api.md) voraussetzt.

#### Vorbereitung

Um auch historische Daten abfragen zu können, muss man dem [agspiel.api.Api](../../agspiel/api/api.py)-Konstruktor seinen API-Key übergeben. Als Datenquelle wird die API von [-Immo-](http://api.agscio.de) verwendet und daher benötigt man auch den dementsprechenden Key. Dies sieht dann folgendermaßen aus:

```python
api = agspiel.api.Api("Deine PHPSESSID", "Dein API-Key")
```

Da die historischen Daten über `date`-Objekte abgefragt werden, muss man sich diese noch über die entsprechende Standardbibliothek importieren:

```python
from datetime import date
```

#### Historische Daten erhalten

Wie im Einführungsabschnitt erklärt, muss man sich nun ein AG-Objekt ausgeben lassen. Dies funktioniert analog zu Einführung, nur kann man nun ein Datum angeben:

```python
ag = api.get_ag(100001, date(2021, 4, 23))
```

Sofern die AG zum angegebenen Zeitpunkt existiert hat und Daten für diesen Zeitpunkt vorhanden sind, ist die Anfrage erfolgreich. Liegt das Datum in der Vergangenheit (was der Sinn dieser Abfrage ist), dann erhält man ein Objekt der Klasse [HistorischeAg](../classes/historischeag.md) mit den Daten vom 23.4.2021. Ist das Datum der heutige Tag, erhält man ein ganz normales Objekt der Klasse [Ag](../classes/ag.md).

#### Hinweise zur Genauigkeit der Daten

Die Daten sollen möglichst den Daten des Tagesabschlusses entsprechen. Da die Daten jedoch täglich zwischen 1-3 Uhr gesammelt werden, kann dies logischerweise nicht zu 100% dem gewünschten Ergebnis entsprechen. Daraus folgt übrigens auch, dass wenn man die Daten für den 23.4.2021 anfragt, man in Wirklichkeit die Daten vom 24.4.2021 um ca. 3 Uhr erhält.
