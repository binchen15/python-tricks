# producer-consumer question

import time
import logging
from concurrent.futures import ThreadPoolExecutor
from threading import Event
from queue import Queue
import random


def producer(q, event):
    """fill the queue 'q' until event is set"""
    while not event.is_set():
        message = random.randint(1, 101)  # [1, 100]
        logging.info(f"produce: {message}")
        q.put(message)
    logging.info("producer quit!")


def consumer(q, event):
    """empty the queue unitl event is set or queue is empty"""
    while not event.is_set() or not q.empty():
        message = q.get()  # block but not raise exception
        logging.info(f"consumer taken {message}")
    logging.info("consumer quit!")


if __name__ == "__main__":
    event = Event()
    que = Queue(maxsize=10)

    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, que, event)
        executor.submit(consumer, que, event)
        time.sleep(0.1)
        logging.info("main thread set the event")
        event.set()
