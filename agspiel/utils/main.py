#  Copyright (c) 2020 | KingKevin23 (@kingkevin023)

from requests import Session

class LoginError(Exception):
    pass

def get_php_session_id(email:str, password:str) -> str:
    """
    Diese Funktion loggt sich im AG-Spiel ein, liest den Cookie "PHPSESSID" aus
    und gibt diesen an den Aufrufer zurück. Für den Fall das die Logindaten
    fehlerhaft sind, wird ein LoginError erzeugt.

    :param email: E-Mail Adresse des AGS-Accounts
    :param password: Passwort des AGS-Accounts
    :raises LoginError: Anmeldedaten sind falsch
    :return: Wert des PHPSESSID Cookies
    """
    request_data = {"email": email, "userpass": password, "permanent": "1", "login": "Einloggen"}
    response = Session().post("https://www.ag-spiel.de/index.php?section=login", data=request_data)
    if "Es gibt keinen Benutzer mit dieser E-Mail!" in response.text:
        raise LoginError("Keinen Benutzer mit dieser Mail!")
    elif "Das Passwort ist nicht korrekt!" in response.text:
        raise LoginError("Falsches Passwort!")
    else:
        return response.cookies.get_dict()["PHPSESSID"]