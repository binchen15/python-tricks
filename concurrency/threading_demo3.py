import logging
import time
import threading

def job(name):
    logging.info(f"thread {name} starting")
    time.sleep(1)
    logging.info(f"thread {name} finished")

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    threads = []
    for i in range(5):
        t = threading.Thread(target=job, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
