# BRUTEFORCEtest

## O projekcie i odpowiedzialność

Ten projekt powstał wyłącznie w celach edukacyjnych oraz w celu pogłębiania wiedzy o cyberbezpieczeństwie i sposobach ochrony przed atakami typu brute-force.  
Część kodu została wygenerowana przy pomocy AI.

**Autor nie ponosi żadnej odpowiedzialności za niewłaściwe wykorzystanie tego narzędzia. Wszelkie działania z użyciem poniższego kodu powinny być prowadzone wyłącznie na własnych zasobach, w środowisku testowym lub za wyraźną zgodą właściciela danej strony!**

---

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
- Automatycznie wykrywa minimalną i maksymalną długość hasła oraz inne reguły pola (pattern, placeholder, title, required – jeśli są dostępne).
- Automatycznie ustawia pozostałe pola formularza (ukryte/checkboxy).
- Próbkuje różne hasła i rozpoznaje sukces po obecności tekstu np. "Wyloguj".
- Przed startem ataku wyświetla wykryte reguły pola hasła oraz wszystkie znalezione pola formularza logowania, aby użytkownik mógł je zweryfikować/nadpisać.

**Uwaga:** Używaj tylko do testów lub za zgodą właściciela strony!

---

## Zaawansowane opcje

- Możesz ręcznie podać nazwy pól loginu, hasła i submit (`--login-field`, `--password-field`, `--submit-field`), nadpisując automatyczną detekcję.
- Możesz ręcznie wymusić minimalną/maksymalną długość hasła (`--min-length`, `--max-length`).
- Program wyświetla ostrzeżenia, jeśli nie uda się wykryć wszystkich reguł automatycznie.

---

## Przykład pełnego uruchomienia

```bash
python main.py \
  --target-url https://example.com/login \
  --username admin \
  --success-string "Logout" \
  --threads 8 \
  --min-length 6 \
  --max-length 12 \
  --login-field user \
  --password-field pass \
  --submit-field submit
```

---

## Zmiany

Zobacz [CHANGELOG.md](CHANGELOG.md) po szczegóły zmian i historii projektu.