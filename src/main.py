import argparse
from src.brute import brute_force

def main():
    parser = argparse.ArgumentParser(description="Brute-force atak na stronę WWW lub API.")
    parser.add_argument('--target-url', required=True, help='Adres URL formularza logowania lub API')
    parser.add_argument('--username', required=True, help='Login użytkownika')
    parser.add_argument('--charset', default='ascii_uppercase+digits', help='Zestaw znaków do zgadywania')
    parser.add_argument('--min-length', type=int, default=1, help='Minimalna długość hasła')
    parser.add_argument('--max-length', type=int, default=8, help='Maksymalna długość hasła')
    parser.add_argument('--threads', type=int, default=4, help='Liczba wątków')
    parser.add_argument('--success-string', required=True, help='Unikalny tekst w odpowiedzi po zalogowaniu (np. "Welcome")')
    parser.add_argument('--fail-string', default='', help='Tekst oznaczający błędne hasło (opcjonalnie)')
    args = parser.parse_args()

    brute_force(
        url=args.target_url,
        username=args.username,
        charset=args.charset,
        min_length=args.min_length,
        max_length=args.max_length,
        threads=args.threads,
        success_string=args.success_string,
        fail_string=args.fail_string
    )

if __name__ == '__main__':
    main()
