# Orderwiderstand einer AG

Wenn ihr euch für das Volumen der Sellorders in einem Prozentbereich über dem aktuellen Briefkurs interessiert (oder das Volumen der Buyorders unter dem aktuellen Briefkurs), könnt ihr dies ganz einfach mit dem folgenden Code tun. In diesem Beispiel lassen wir uns das Volumen aller Sellorder der King Kompany (WKN 175353) ausgeben, die maximal 5 Prozent über dem aktuellen Briefkurs liegen.

```python
from agspiel.api import Api

wkn = 175353 # Die betrachtete AG
buy = False # Ob das Buy- oder Sellwiderstand betrachtet werden soll
prozent = 5 # Die Abweichung vom Geld- bzw. Briefkurs in Prozent

api = Api("Deine PHPSESSID")
ag = api.get_ag(wkn)
orderbuch = ag.orders
if buy:
    stop = ag.geld
    start = stop * (1 - (prozent / 100))
    typ = "buy"
else:
    start = ag.brief
    stop = start * (1 + (prozent / 100))
    typ = "sell"

relevante_orders = [order for order in orderbuch if order.typ == typ]
volumen = 0
for order in relevante_orders:
    if start <= order.limit <= stop:
        volumen += order.limit * order.stueckzahl

print(volumen)
```

In diesem Beispiel könntet ihr die den Parameter `phpsessid` von der Klasse Api sogar weglassen, da die Orderbuchdaten aus der API von Rady geholt werden und hier somit keine Verfikation gegenüber dem AGS-Server erforderlich ist.
