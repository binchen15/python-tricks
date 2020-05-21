# context_manager.demo
# ref. https://dbader.org/blog/python-context-managers-and-with-statement
 
class Indent(object):
	def __init__(self):
		self.level = 0

	def __enter__(self):
		self.level += 1
		return self

	def __exit__(self,exc_type, exc_val, exc_tb):
		self.level -= 1

	def print(self, text):
		print("    " * self.level + text)


if __name__ == "__main__":
	print("Entering indent context manager:")
	with Indent() as indentor: 
        # with Indent() called __init__() then __enter__()
		indentor.print("HI")
		with indentor:  # calls __enter__()
			indentor.print("John")
			with indentor:
				indentor.print("Doe")
		indentor.print("Bye!")



