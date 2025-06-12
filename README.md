# BRUTEFORCEtest

Program do brute-force na stronach WWW/API bez znajomości hasła ani jego hasha.

## Uruchamianie

```bash
pip install -r requirements.txt

python main.py \
  --target-url https://twojastrona.pl/login \
  --username admin \
  --charset ascii_uppercase+digits \
  --min-length 5 \
  --max-length 5 \
  --threads 4 \
  --success-string "Zalogowano pomyślnie"
```

**Wskazówki:**
- `--target-url` – adres endpointa logowania
- `--username` – login użytkownika
- `--success-string` – unikalny tekst pojawiający się po poprawnym logowaniu (np. "Welcome" lub "Panel")
- `--fail-string` – (opcjonalne) tekst, który oznacza błędne hasło

**Uwaga:** Przed użyciem sprawdź legalność testów na danej stronie!
