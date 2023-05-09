# Hilfsfunktionen

Im Folgenden sind einige Hilfsfunktionen beschrieben, die die Benutzung der API angenehmer gestalten sollen.

#### Authentisierung mit E-Mail und Passwort

Um nicht jedes Mal die aktuelle PHPSESSID aus seinem Browser in sein Skript kopieren zu müssen gibt es innerhalb der [agspiel.utils](https://github.com/KingKevin23/agspiel-python-api/tree/master/agspiel/utils)-Paketes die Funktion `get_php_session_id`. Diese akzeptiert die E-Mail-Adresse und das Passwort eines Nutzers und holt sich automatisch eine gültige PHPSESSID:

```python
import agspiel

session_id = agspiel.utils.get_php_session_id("DEINE E_MAIL", "DEIN PASSWORT")
api = agspiel.api.Api(session_id)
```

Der gesamte Code dieser Funktion kann auf [GitHub](../../agspiel/utils/main.py) oder nach erfolgreicher Installation auch auf dem eigenen Gerät überprüft werden.&#x20;
