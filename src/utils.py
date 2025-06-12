import itertools
import string
import threading
from queue import Queue

# Zestawy znaków predefiniowane
SUPPORTED_CHARSETS = {
    "ascii_lowercase": string.ascii_lowercase,
    "ascii_uppercase": string.ascii_uppercase,
    "digits": string.digits,
    "ascii_letters": string.ascii_letters,
    "ascii_lowercase_digits": string.ascii_lowercase + string.digits,
    "ascii_lowercase_digits_special": string.ascii_lowercase + string.digits + "!@#$%^&*()-_+=",
    "full_ascii": string.ascii_letters + string.digits + string.punctuation,
}

def brute_force_search(data, target):
    """Brute-force wyszukiwanie wartości w liście."""
    for idx, item in enumerate(data):
        if item == target:
            return idx
    return -1

def _password_worker(password, charset, max_length, task_queue, found_event, result_holder):
    while not found_event.is_set():
        try:
            length, prefix = task_queue.get(timeout=0.1)
        except Exception:
            break
        for comb in itertools.product(charset, repeat=length - len(prefix)):
            guess = prefix + ''.join(comb)
            if found_event.is_set():
                break
            if guess == password:
                result_holder.append(guess)
                found_event.set()
                break
        task_queue.task_done()

def brute_force_password_multithreaded(password, charset="ascii_lowercase_digits_special", max_length=4, num_threads=4):
    """
    Brute-force łamanie hasła z wielowątkowością.
    """
    if charset in SUPPORTED_CHARSETS:
        charset = SUPPORTED_CHARSETS[charset]
    else:
        charset = string.ascii_lowercase
    found_event = threading.Event()
    result_holder = []
    task_queue = Queue()

    # Podziel zadania na prefiksy długości 1 dla równoległości
    for length in range(1, max_length + 1):
        for prefix in itertools.product(charset, repeat=1):
            task_queue.put((length, ''.join(prefix)))

    threads = []
    for _ in range(num_threads):
        t = threading.Thread(
            target=_password_worker,
            args=(password, charset, max_length, task_queue, found_event, result_holder)
        )
        t.daemon = True
        t.start()
        threads.append(t)

    task_queue.join()
    found_event.set()
    for t in threads:
        t.join(timeout=0.1)
    return result_holder[0] if result_holder else None
