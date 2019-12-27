from contextlib import contextmanager
from threading import Lock, Thread
DATA = {'old_item_0': 0, 'old_item_1': 1, 'old_item_2': 2, 'old_item_3': 3}


class RWLock:
    def __init__(self):
        self.write_lock = Lock()
        self.read_lock = Lock()
        self.readers = 0

    def acquire_read(self):
        self.read_lock.acquire()
        try:
            self.readers += 1
            # як тільки з'являєтсья перший читач, блокуємо write lock
            if self.readers == 1:
                self.write_lock.acquire()
        finally:
            self.read_lock.release()

    def release_read(self):
        self.read_lock.acquire()
        try:
            self.readers -= 1
            # якщо залишається 0 читачів, вивільняємо write lock
            if self.readers == 0:
                self.write_lock.release()
        finally:
            self.read_lock.release()

    @contextmanager
    def read_locked(self):
        try:
            self.acquire_read()
            yield
        finally:
            self.release_read()

    def acquire_write(self):
        self.write_lock.acquire()

    def release_write(self):
        self.write_lock.release()

    @contextmanager
    def write_locked(self):
        try:
            self.acquire_write()
            yield
        finally:
            self.release_write()


def read_data(_lock, thread_id):
    with _lock.read_locked():
        items = list(DATA.keys())
        thread_item = thread_id % len(DATA)
        print(f"Thread number {thread_id} get item number {items[thread_item]} with value {DATA[items[thread_item]]}")


def write_data(_lock, thread_id):
    with _lock.write_locked():
        data_len = len(DATA)
        thread_key = 'new_item_' + str(data_len + thread_id - 1) + '_thread_num_' + str(thread_id)
        DATA[thread_key] = thread_id


if __name__ == '__main__':
    lock = RWLock()

    for x in range(5):
        thread = Thread(target=write_data, args=(lock, x))
        thread.start()
        thread.join()

    for x in range(20):
        thread = Thread(target=read_data, args=(lock, x))
        thread.start()
        thread.join()