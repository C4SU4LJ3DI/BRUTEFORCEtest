import argparse
from utils import (
    brute_force_search,
    brute_force_password_multithreaded,
    SUPPORTED_CHARSETS,
)
from colorama import Fore, Style, init as colorama_init

colorama_init(autoreset=True)

def load_data(filepath, verbose=False):
    try:
        with open(filepath, "r") as f:
            lines = f.readlines()
        if verbose:
            print(Fore.BLUE + f"[VERBOSE] Wczytano {len(lines)} linii z pliku {filepath}")
        return [int(line.strip()) for line in lines if line.strip()]
    except FileNotFoundError:
        print(f"[ERROR] Plik {filepath} nie istnieje!")
        exit(1)
    except Exception as e:
        print(f"[ERROR] Wystąpił nieoczekiwany błąd: {e}")
        exit(1)

def main():
    parser = argparse.ArgumentParser(description="Advanced Brute Force Tool")
    parser.add_argument(
        "--mode", choices=["search", "password"], required=True,
        help="Tryb działania: wyszukiwanie liczby lub brute-force hasła",
    )
    parser.add_argument("--target", required=True, help="Liczba (search) lub hasło (password)")
    parser.add_argument("--input", help="Plik wejściowy z liczbami (dla --mode search)")
    parser.add_argument("--charset", choices=SUPPORTED_CHARSETS.keys(), default="ascii_lowercase_digits_special",
                        help="Zestaw znaków do brute-force hasła")
    parser.add_argument("--max-length", type=int, default=4, help="Maksymalna długość hasła (password mode)")
    parser.add_argument("--threads", type=int, default=4, help="Liczba wątków (password mode)")
    parser.add_argument("--verbose", action="store_true", help="Wyświetlaj dodatkowe informacje diagnostyczne")
    args = parser.parse_args()

    if args.mode == "search":
        if not args.input:
            print(Fore.RED + "Musisz podać --input z plikiem wejściowym!")
            exit(1)
        data = load_data(args.input, verbose=args.verbose)
        try:
            target = int(args.target)
        except ValueError:
            print(Fore.RED + "Podany target nie jest liczbą!")
            exit(1)
        if args.verbose:
            print(Fore.BLUE + f"[VERBOSE] Szukam liczby {target} w {len(data)} elementach.")
        idx = brute_force_search(data, target, verbose=args.verbose)
        if idx != -1:
            print(Fore.GREEN + f"Znaleziono liczbę {args.target} pod indeksem {idx}")
        else:
            print(Fore.YELLOW + f"Liczba {args.target} nie została znaleziona.")

    elif args.mode == "password":
        if args.verbose:
            print(Fore.BLUE + f"[VERBOSE] Brute-force hasła '{args.target}' z charsetem '{args.charset}' do długości {args.max_length} ({args.threads} wątki)...")
        found = brute_force_password_multithreaded(
            args.target,
            charset=args.charset,
            max_length=args.max_length,
            num_threads=args.threads,
            verbose=args.verbose,
        )
        if found:
            print(Fore.GREEN + f"Hasło złamane: {found}")
        else:
            print(Fore.RED + f"Nie udało się złamać hasła w zadanym zakresie.")

if __name__ == "__main__":
    main()
    