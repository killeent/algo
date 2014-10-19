from __future__ import print_function

"""
Original Author: Trevor Killeen (2014)

Prints all possible subsets of the numbers 1...n 
"""

def backtrack(vector, s, k, n):
	"""
	backtrack helps generate all subsets by recursively generating solutions.

	vector:	represents the current state of the world. It is a list of at most
	size n, where vector[i] = true if element i is in the subset, or false
	if element i is not in the subset

	s: the list of subsets we have seen thus far

	k: the position in the vector which we are considering at this position

	n: the size of the set we are generating subsets of
	"""	

	if (k == n):
		return s
	else:
		for i in range(0, 2):
			vector.append(True if i == 0 else False)
			s = print_subset(vector, s, k)
			s = backtrack(vector, s, k+1, n)
			vector.pop(k-1)
		return s

def print_subset(vector, s, k):
	"""
	prints the subset of 1...k represent by vector if it is not in the set s
	"""
	output = list()
	for i in range(1, k+1):
		if vector[i-1]:
			output.append(i)
	if output not in s:
		print(output)
		s.append(output)
	return s

def main():
	n = int(raw_input("Enter a number: "))
	backtrack(list(), list(), 1, n+1)


if __name__ == '__main__':
	main()