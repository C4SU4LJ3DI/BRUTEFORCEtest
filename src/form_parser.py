import requests
from bs4 import BeautifulSoup

def guess_login_form(url):
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

    return {
        "action": form.get("action") or url,
        "login_field": login_field,
        "password_field": password_field,
        "submit_field": submit_field,
        "extra_fields": extra_fields,
        "method": (form.get("method") or "post").lower()
    }

def guess_password_rules(form_soup, password_field):
    # Spróbuj wykryć ograniczenia na polu hasła
    pw_input = form_soup.find("input", {"name": password_field})
    minlen = int(pw_input.get("minlength", 4)) if pw_input else 4
    maxlen = int(pw_input.get("maxlength", 12)) if pw_input else 12
    # Możesz tutaj rozbudować o wykrywanie pattern, required, etc.
    return minlen, maxlen
