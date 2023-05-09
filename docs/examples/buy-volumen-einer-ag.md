# Buy Volumen einer AG

Wenn ihr euch das gesamte Buyvolumen im Orderbuch einer AG ausgeben lassen möchtet, könnt ihr dies über den folgenden Code tun. In diesem Beispiel lassen wir uns das Buyvolumen von Rady (WKN 100001) ausgeben.

```python
from agspiel.api import Api

api = Api("DEINE PHPSESSID")
ag = api.get_ag(100001)
buyvolumen = 0

for order in ag.orders:
    if order.typ == "buy":
        buyvolumen += order.limit * order.stueckzahl

print(buyvolumen)
```

In diesem Beispiel könntet ihr die den Parameter `phpsessid` von der Klasse Api sogar weglassen, da die Orderbuchdaten aus der API von Rady geholt werden und hier somit keine Verfikation gegenüber dem AGS-Server erforderlich ist.
