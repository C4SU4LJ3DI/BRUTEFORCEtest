import requests
from bs4 import BeautifulSoup

def guess_login_form(url):
    """
    Wykrywa podstawowe informacje o formularzu logowania oraz analizuje pole hasła,
    próbując wydobyć jak najwięcej metadanych (np. długość, pattern, placeholder, title).
    """
    r = requests.get(url, timeout=8, allow_redirects=True)
    soup = BeautifulSoup(r.text, "lxml")
    form = soup.find("form")
    if not form:
        raise Exception("Nie znaleziono formularza na stronie.")

    inputs = form.find_all("input")
    login_field = None
    password_field = None
    submit_field = None
    extra_fields = {}

    # Najczęstsze nazwy pól
    login_names = ["username", "login", "user", "email"]
    password_names = ["password", "pass", "passwd"]
    submit_types = ["submit"]

    for inp in inputs:
        inp_type = inp.get("type", "").lower()
        inp_name = inp.get("name", "")
        if not login_field and inp_name and any(n in inp_name.lower() for n in login_names):
            login_field = inp_name
        elif not password_field and inp_name and any(n in inp_name.lower() for n in password_names):
            password_field = inp_name
        elif inp_type in submit_types or inp.get("value", "").lower() in ["login", "zaloguj"]:
            submit_field = inp_name or inp.get("value", "")

        # Ukryte i inne domyślnie dołączane
        if inp_type in ("hidden", "checkbox") and inp_name:
            extra_fields[inp_name] = inp.get("value", "")

    # Uzupełnianie domyślne jeśli nie wykryto
    if not login_field and inputs:
        login_field = inputs[0].get("name", "")
    if not password_field and inputs:
        for inp in inputs:
            if inp.get("type") == "password":
                password_field = inp.get("name", "")
                break

    # Pobierz więcej informacji o polu hasła
    password_info = get_password_field_info(soup, password_field)

    return {
        "action": form.get("action") or url,
        "login_field": login_field,
        "password_field": password_field,
        "submit_field": submit_field,
        "extra_fields": extra_fields,
        "method": (form.get("method") or "post").lower(),
        "password_info": password_info,
    }

def get_password_field_info(soup, password_field):
    """
    Zwraca informacje o polu hasła: minlength, maxlength, pattern, placeholder, title, required.
    """
    info = {}
    pw_input = soup.find("input", {"name": password_field})
    if not pw_input:
        return info
    info["minlength"] = int(pw_input.get("minlength", 4)) if pw_input.get("minlength") else 4
    info["maxlength"] = int(pw_input.get("maxlength", 12)) if pw_input.get("maxlength") else 12
    info["pattern"] = pw_input.get("pattern", None)
    info["placeholder"] = pw_input.get("placeholder", None)
    info["title"] = pw_input.get("title", None)
    info["required"] = pw_input.has_attr("required")
    return info

def guess_password_rules(form_soup, password_field):
    """
    Wykrywa ograniczenia oraz metadane na polu hasła: minlength, maxlength, pattern, placeholder, title, required.
    Zwraca słownik z tymi informacjami.
    """
    info = {}
    pw_input = form_soup.find("input", {"name": password_field})
    if not pw_input:
        # Wartości domyślne
        info["minlength"] = 4
        info["maxlength"] = 12
        info["pattern"] = None
        info["placeholder"] = None
        info["title"] = None
        info["required"] = False
        return info
    info["minlength"] = int(pw_input.get("minlength", 4)) if pw_input.get("minlength") else 4
    info["maxlength"] = int(pw_input.get("maxlength", 12)) if pw_input.get("maxlength") else 12
    info["pattern"] = pw_input.get("pattern", None)
    info["placeholder"] = pw_input.get("placeholder", None)
    info["title"] = pw_input.get("title", None)
    info["required"] = pw_input.has_attr("required")
    return info