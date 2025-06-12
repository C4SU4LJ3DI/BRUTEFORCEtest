# BRUTEFORCEtest
# testowanie możliwości / cyberbezpieczeństwa / TYLKO DO LEGALNEGO UŻYTKU / testowanie kodowania AI

# Projekt: Bruteforce (zaawansowany)

Bardzo zaawansowany projekt demonstrujący algorytmy brute-force, wielowątkowość i testy automatyczne.

## Funkcje

- Tryb brute-force wyszukiwania liczby w pliku (search)
- Tryb łamania hasła (password) z obsługą znaków specjalnych, wielowątkowością i wyborem charsetu
- Automatyczne testy (pytest)
- Kolorowe wyjście (colorama)
- Czytelna struktura i łatwość rozbudowy

## Instalacja

Wymagany Python 3.8+
```bash
pip install -r requirements.txt
```

## Użycie

### Tryb brute-force search (wyszukiwanie liczby):
```bash
python src/main.py --mode search --target 42 --input examples/sample_input.txt
```

### Tryb brute-force password:
```bash
python src/main.py --mode password --target abc --charset ascii_lowercase --max-length 3 --threads 4
python src/main.py --mode password --target '5' --charset digits --max-length 1 --threads 2
python src/main.py --mode password --target '!' --charset ascii_lowercase_digits_special --max-length 1 --threads 2
```

Dostępne zestawy znaków (`--charset`):
- ascii_lowercase
- ascii_uppercase
- digits
- ascii_letters
- ascii_lowercase_digits
- ascii_lowercase_digits_special
- full_ascii

## Testy

```bash
pytest
```

## Przykładowa baza SQL

Zobacz plik: `database/schema.sql`
