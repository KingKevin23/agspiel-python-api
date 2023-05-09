# Indexanteile an AG

Wenn ihr euch für die Aktionärsstruktur einer AG nach Indizes interessiert (etwa um einen möglichen Übernahmeschutz durch den eigenen Index zu überprüfen), könnt ihr euch dies mithilfe des folgenden Codes (am Beispiel der BEST AG ([#140818](https://www.ag-spiel.de/index.php?section=profil\&aktie=140818))) auch grafisch anzeigen lassen. Hierzu benötigt ihr noch das `matplotlib` Paket, welches ihr wie diese Python-API mit dem Kommandozeilenbefehl `pip install matplotlib` installieren könnt.

```python
from agspiel.api import Api
from matplotlib import pyplot as plot

api = Api("Deine PHPSESSID")
ag = api.get_ag(140818)
aktionaersstruktur = ag.aktionaere
aktienanzahl = ag.aktienanzahl
minimum = int(aktienanzahl * 0.05)

indizes = {}

# Ermittelt die Aktien die jeder Index an AG hält
for i in aktionaersstruktur:
    aktionaer = api.get_ag(i.wkn)
    try:
        name = aktionaer.ceo.index.name
    except AttributeError:
        name = "Indexlos"
    try:
        indizes[name] += i.stueckzahl
    except KeyError:
        indizes[name] = i.stueckzahl

counter = 0
to_delete = []

# Ermittelt alle Indizes kleiner als 5%
for k, v in indizes.items():
    if v < minimum:
        to_delete.append(k)
        counter += v

# Entfernt alle zu kleinen Indizes
for i in to_delete:
    del indizes[i]

labels = ["Andere"]
sizes = [counter]

for k in sorted(indizes, key=indizes.get):
    labels.append(k)
    sizes.append(indizes[k])

# Nun wird ein Kreisdiagramm erzeugt
fig1, ax1 = plot.subplots()
ax1.pie(sizes, labels=labels, startangle=90, autopct='%1.1f%%')
ax1.axis("equal")
plot.show()
```

Wenn wir diesen Code nun ausführen, erhalten wir für die Aktionärsstruktur der BEST AG ([#140818](https://www.ag-spiel.de/index.php?section=profil\&aktie=140818)) die folgende Verteilung nach Indizes:

![Ergebnis](https://i.ibb.co/sbJCfdK/test.png)

In diesem Beispiel könntet ihr die den Parameter phpsessid von der Klasse Api sogar weglassen, da alle Daten aus der API von Rady geholt werden und hier somit keine Verfikation gegenüber dem AGS-Server erforderlich ist.
