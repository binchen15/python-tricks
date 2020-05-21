# a generator of palindrome numbers
# ref: https://realpython.com/introduction-to-python-generators/

# list comprehensions can be faster to evaluate than the equivalent generator expression. 

# StopIteration exception

#Generator functions use the Python yield keyword instead of return
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1


def is_palindrome(num):
    if num // 10 == 0:
        return True
    temp = num
    reversed_num = 0

    while temp != 0:
        reversed_num = (reversed_num * 10) + (temp % 10)
        temp = temp // 10

    if num == reversed_num:
        return num
    else:
        return False

if __name__ == "__main__":
	for i in infinite_sequence():
		pal = is_palindrome(i)
		if pal:
			print(pal)

