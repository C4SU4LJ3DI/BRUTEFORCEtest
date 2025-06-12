import requests

def try_password(url, username, password, success_string, fail_string):
    # Dostosuj do formatu logowania na stronie!
    data = {
        "username": username,
        "password": password
    }
    try:
        r = requests.post(url, data=data, timeout=5)
        # Jeśli zalogowanie się powiodło, w odpowiedzi powinien być success_string
        if success_string in r.text and (not fail_string or fail_string not in r.text):
            return True
    except Exception as e:
        pass
    return False
