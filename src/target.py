import requests

def try_password(url, username, password, success_string, fail_string,
                 login_field, password_field, submit_field, extra_fields, method):
    data = {}
    if login_field:
        data[login_field] = username
    if password_field:
        data[password_field] = password
    if submit_field:
        data[submit_field] = "Zaloguj"
    if extra_fields:
        data.update(extra_fields)

    try:
        if method == "post":
            r = requests.post(url, data=data, timeout=5, allow_redirects=True)
        else:
            r = requests.get(url, params=data, timeout=5, allow_redirects=True)
        if success_string in r.text and (not fail_string or fail_string not in r.text):
            return True
    except Exception:
        pass
    return False
