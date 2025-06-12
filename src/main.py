import argparse
from utils import (
    brute_force_search,
    brute_force_password_multithreaded,
    SUPPORTED_CHARSETS,
)
from colorama import Fore, Style, init as colorama_init

colorama_init(autoreset=True)

def load_data(filepath):
    with open(filepath, "r") as f:
        return [int(line.strip()) for line in f.readlines()]

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

    args = parser.parse_args()

    if args.mode == "search":
        if not args.input:
            print(Fore.RED + "Musisz podać --input z plikiem wejściowym!")
            exit(1)
        data = load_data(args.input)
        try:
            target = int(args.target)
        except ValueError:
            print(Fore.RED + "Podany target nie jest liczbą!")
            exit(1)
        idx = brute_force_search(data, target)
        if idx != -1:
            print(Fore.GREEN + f"Znaleziono liczbę {args.target} pod indeksem {idx}")
        else:
            print(Fore.YELLOW + f"Liczba {args.target} nie została znaleziona.")

    elif args.mode == "password":
        print(Fore.CYAN + f"Brute-force hasła '{args.target}' z charsetem '{args.charset}' do długości {args.max_length} ({args.threads} wątki)...")
        found = brute_force_password_multithreaded(
            args.target,
            charset=args.charset,
            max_length=args.max_length,
            num_threads=args.threads,
        )
        if found:
            print(Fore.GREEN + f"Hasło złamane: {found}")
        else:
            print(Fore.RED + f"Nie udało się złamać hasła w zadanym zakresie.")

if __name__ == "__main__":
    main()
