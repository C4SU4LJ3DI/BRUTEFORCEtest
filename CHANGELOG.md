

# Changelog

## [Unreleased]

### Dodano
- `guess_login_form` zwraca teraz słownik `password_info` z informacjami o polu hasła (`minlength`, `maxlength`, `pattern`, `placeholder`, `title`, `required`).
- Dodano funkcję `get_password_field_info`, która wydobywa dodatkowe informacje o polu hasła.
- Funkcja `guess_password_rules` może teraz zwracać także `pattern` (jeśli jest obecny).
- Dodano docstringi i komentarze opisujące cel i działanie każdej funkcji.

### Poprawiono
- Ulepszono wykrywanie pól loginu i hasła oraz informacji o formularzu logowania.

---

## [Starsze wersje]

*(Brak wpisów dla wcześniejszych wersji - był problem z ulokowaniem zmian, raczej się nie zapisały, ale było ich wiele)*

# Changelog początkowe

## [0.1.0] - 2025-06-12
### Added
- Początkowa wersja projektu
- Testy automatyczne
- Tryb search i password
- GitHub Actions CI

### Removed
- Nieużywane katalogi bazy danych
