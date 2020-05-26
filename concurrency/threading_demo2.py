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

    t = threading.Thread(target=job, args=(1,), daemon=True)
    logging.info("main starts")
    t.start()
    logging.info("main finished")
    logging.info("main will not wait for daemon thread, must be joined")
    t.join()
