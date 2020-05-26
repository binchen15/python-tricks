import logging
import time
from concurrent.futures import ThreadPoolExecutor


def job(name):
    logging.info(f"thread {name} starting")
    time.sleep(1)
    logging.info(f"thread {name} finished")


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    # context manager will call .join()
    with ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(job, range(6))
