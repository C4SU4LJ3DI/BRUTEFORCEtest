import itertools
import string
import threading

# Obsługiwane zestawy znaków dla brute-force
SUPPORTED_CHARSETS = {
    "ascii_lowercase": string.ascii_lowercase,
    "ascii_uppercase": string.ascii_uppercase,
    "digits": string.digits,
    "ascii_letters": string.ascii_letters,
    "ascii_lowercase_digits": string.ascii_lowercase + string.digits,
    "ascii_lowercase_digits_special": string.ascii_lowercase + string.digits + "!@#$%^&*",
    "full_ascii": string.ascii_letters + string.digits + string.punctuation,
}

def brute_force_search(data, target, verbose=False):
    """Przeszukuje listę data w poszukiwaniu target, zwraca indeks lub -1."""
    for idx, val in enumerate(data):
        if verbose:
            print(f"[VERBOSE] Sprawdzam indeks {idx}: {val}")
        if val == target:
            return idx
    return -1

def brute_force_password_multithreaded(password, charset="ascii_lowercase_digits_special", max_length=4, num_threads=4, verbose=False):
    """Brute-force hasła rozdzielony na wątki."""
    charset_str = SUPPORTED_CHARSETS[charset]
    found_result = {"found": None}
    lock = threading.Lock()
    stop_event = threading.Event()

    def worker(start_length, step):
        for length in range(start_length, max_length + 1, step):
            if verbose:
                print(f"[VERBOSE] Wątek {threading.current_thread().name} sprawdza długość {length}")
            for attempt in itertools.product(charset_str, repeat=length):
                if stop_event.is_set():
                    return
                attempt_str = ''.join(attempt)
                if verbose and length <= 2:
                    print(f"[VERBOSE] Próba: {attempt_str}")
                if attempt_str == password:
                    with lock:
                        found_result["found"] = attempt_str
                        stop_event.set()
                    return

    threads = []
    for i in range(num_threads):
        t = threading.Thread(target=worker, args=(i+1, num_threads), name=f"Thread-{i+1}")
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    return found_result["found"]
