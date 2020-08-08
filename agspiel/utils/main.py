#  Copyright (c) 2020 | KingKevin23 (@kingkevin023)

from webbot import Browser

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
    web = Browser(showWindow=False)
    web.go_to("https://www.ag-spiel.de/index.php?section=login")
    web.type(email, into="email")
    web.type(password, into="password", id="userpass")
    web.click("Einloggen")
    if "Du bist eingeloggt" in web.driver.page_source:
        for i in web.driver.get_cookies():
            if i.get("name") == "PHPSESSID":
                return i.get("value")
    elif "Es gibt keinen Benutzer mit dieser E-Mail!" in web.driver.page_source:
        raise LoginError("Keinen Benutzer mit dieser Mail!")
    elif "Das Passwort ist nicht korrekt!" in web.driver.page_source:
        raise LoginError("Falsches Passwort!")
    else:
        raise LoginError("Weder eingeloggt, noch Passwort oder Mail falsch!")