from __future__ import print_function

def fibonacci(n):
	"""
	Calculates the nth fibonacci number using dynamic programming!
	"""
	back2 = 0;
	back1 = 1;

	if n == 0:
		return 0

	for i in range (2, n):
		cur = back1 + back2
		back2 = back1
		back1 = cur

	return back1 + back2

def main():
	n = int(raw_input("What Fibonacci Number would you like to know: "))
	print(fibonacci(n))

if __name__ == '__main__':
	main()