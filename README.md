# BRUTEFORCEtest

Brute-force na stronach WWW bez znajomości pól formularza/logowania — automatyczna detekcja!

## Instalacja

```bash
pip install -r requirements.txt
```

## Użycie

Podstawowa komenda (wszystko wykrywa się automatycznie):

```bash
python main.py --target-url https://libre.forumpolish.com/login --username Admin --success-string "Wyloguj"
```

Opcje zaawansowane (możesz nadpisać domyślne wykrywanie):

```bash
python main.py --target-url ... --username ... --min-length 5 --max-length 8 --login-field login --password-field pass
```

### Co robi program?
- Wykrywa automatycznie pola loginu i hasła w formularzu logowania.
- Automatycznie wykrywa minimalną i maksymalną długość hasła (jeśli możliwe).
- Automatycznie ustawia pozostałe pola formularza (ukryte/checkboxy).
- Próbkuje różne hasła i rozpoznaje sukces po obecności tekstu np. "Wyloguj".

**Uwaga:** Używaj tylko do testów lub za zgodą właściciela strony!
