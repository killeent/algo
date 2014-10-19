"""
Original Author: Trevor Killeen (2014)

Prints all possible permutations of the numbers 1...n 
"""

def backtrack(vector, k, n):
	"""
	backtrack generates all permutations by recursively generating solutions.

	vector:	represents the current state of the world. It is a list of at most
	size n, where vector[i] = some number between 1 and n and is part of the
	active permutation being generated

	s: the list of subsets we have seen thus far

	n: the size of the set we are generating subsets of
	"""
	if k == n:
		print(vector)
	else:
		candidates = [i for i in range(1, n) if i not in vector]
		for c in candidates:
			vector.append(c)
			backtrack(vector, k+1, n)
			vector.pop(k-1)

def main():
	n = int(raw_input("Enter a number: "))
	backtrack(list(), 1, n+1)

if __name__ == '__main__':
	main()