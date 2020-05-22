# deqeue is threadsafe

from collections import deque
from threading import Thread
import time 
import random

candle = deque(range(100))

def consumer(direction, func):
	while True:
		try:
			val = func() # pop(), or popleft()
			time.sleep(0.01*random.randint(1,10))
		except IndexError:
			break
		else:
			print("{}: {}".format(direction, val))
	print("{}: Done!".format(direction))

t1 = Thread(target=consumer, args=("left",  candle.popleft) )
t2 = Thread(target=consumer, args=("right", candle.pop) )

t1.start()
t2.start()
t1.join()
t2.join()


