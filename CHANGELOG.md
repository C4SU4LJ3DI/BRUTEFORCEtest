# Changelog

## [Unreleased]

### Dodano
- Automatyczne wykrywanie pól formularza logowania na podstawie HTML (funkcja `guess_login_form`).
- Funkcja `guess_login_form` zwraca teraz pełny słownik z informacjami o formularzu, w tym:
  - Nazwa pola loginu (`login_field`)
  - Nazwa pola hasła (`password_field`)
  - Nazwa pola/przycisku submit (`submit_field`)
  - Dodatkowe pola (`extra_fields`)
  - Metoda przesyłania (`method`)
  - Szczegółowe informacje o polu hasła w pod-słowniku `password_info` (`minlength`, `maxlength`, `pattern`, `placeholder`, `title`, `required`).
- Dodano funkcję `get_password_field_info`, która wydobywa metadane i ograniczenia pola hasła.
- Funkcja `guess_password_rules` zwraca słownik z pełnymi regułami dotyczącymi pola hasła: `minlength`, `maxlength`, `pattern`, `placeholder`, `title`, `required`.
- Rozszerzono obsługę detekcji popularnych nazw pól loginu i hasła (np. user, email, pass, passwd).
- Zintegrowano automatyczne pobieranie reguł hasła z formularza oraz możliwość ich nadpisania przez argumenty CLI.
- Dodano wyświetlanie w konsoli wykrytych reguł pola hasła i wszystkich znalezionych pól formularza przed rozpoczęciem ataku brute-force.
- Dodano docstringi i komentarze opisujące cel i działanie każdej funkcji.
- Umożliwiono podanie nazw pól loginu, hasła i submit przez argumenty CLI (z nadpisywaniem automatycznej detekcji).
- Ulepszono komunikaty diagnostyczne i ostrzeżenia w przypadku braku wykrycia wszystkich reguł.

### Poprawiono
- Ulepszono wykrywanie pól loginu, hasła oraz informacji o formularzu logowania nawet przy nietypowych układach HTML.
- Poprawiono domyślne wartości długości hasła, gdy nie uda się ich wykryć automatycznie.
- Poprawiono czytelność kodu (lepsze formatowanie, typowanie, opisanie funkcji).

---

## [0.1.0] - 2025-06-12

### Dodano
- Początkowa wersja projektu.
- Testy automatyczne.
- Tryb search i password.
- GitHub Actions CI.

### Usunięto
- Nieużywane katalogi bazy danych.