import logging
import time
from concurrent.futures import ThreadPoolExecutor
from threading import Lock

class FakeDatabase:
    def __init__(self):
        self.value = 0
        self._lock = Lock()

    def update(self, name):
        with self._lock:  # call .acquire and .release automatically
            local_copy = self.value  # retrieve db
            local_copy += 1          # work....
            time.sleep(0.1)
            self.value = local_copy  # save to db


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    db = FakeDatabase()

    # context manager will call .join()
    with ThreadPoolExecutor(max_workers=3) as executor:
        for i in range(3):
            # .submit(function, *args, **kwargs)
            executor.submit(db.update, i)
    print(db.value)


