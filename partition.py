"""
Partitions a list of n={s1, ..., sn} integers into k subsequences without 
reordering such that the maximum sum of any range is minimized.

We define M(n, k) to be the minimum cost over all possible partitionings of
the n numbers into k ranges. M(n, k) can be calculated as follows:

M(n, k) = min(i = 1...n) max(M(i, k-1), sum(j = i+1 ... n)sj)

That is M(n, k) is the searches through the n possible choices of placing
a partition, and picks the one that minimizes the cost of the paritioning.
This cost is the maximum of the cost of the partition to the left, and the
remaining the sum to the right. 

We define two base cases:

1. M(1, k) = s1, that is the cost of partitoning a single item into k
partitions is the cost of that item

2. M(n, 1) = s1 + s2 + ... sn, that is the cost of partitioning n numbers
into 1 partition is the sum of those numbers

With this recurrence relation we can calculate M(n, k) for any n, k and
subsequence dynamically in O(kn^2) time.
"""

from __future__ import print_function
from sys import maxint

def partition(s, n, k):
	"""
	Partitions s into k partitions that minimize the maximum cost of any
	partition, as described above.

	s: a list of n integers
	"""
	m = [[0 for x in range(n+1)] for x in range(n+1)]
	d = [[0 for x in range(n+1)] for x in range(n+1)]
	p = [0 for x in range(n+1)]

	# First we create a prefix sum of the values in s. This improves
	# performance down the road
	p[0] = 0
	for i in range(1, n+1):
		p[i] = p[i-1] + s[i]

	# Next we initialize the base cases described above
	for i in range(1, n+1):
		m[i][1] = p[i]
	for i in range(1, k+1):
		m[1][i] = s[1]

	# now we can evaluate our recurrence. We start at M(2, 2) because
	# this is the first such value filled in. We then fill in first
	# by increasing partition count, then by increasing sequence
	for i in range(2, n+1):
		for j in range(2, k+1):
			m[i][j] = maxint
			# try all possible partition locations
			for x in range(1, i):
				cost = max(m[x][j-1], p[i]-p[x])
				if (m[i][j] > cost):
					m[i][j] = cost
					# store the optimal partition location
					d[i][j] = x

	# now that we have calcuated the optimal partitions for all
	# combinations of 1...n, 1...k , lets actually determine the 
	# partition for our particular input
	reconstruct(s, d, n, k)

def reconstruct(s, d, n, k):
	"""
	Prints the partitions line by line
	"""
	if k == 1:
		print_partition(s, 1, n)
	else:
		reconstruct(s, d, d[n][k], k-1)
		print_partition(s, d[n][k]+1, n)

def print_partition(s, start, end):
	for i in range(start, end+1):
		print(s[i], end='')
	print()


def main():
	n = int(raw_input("how many numbers?: "))
	k = int(raw_input("how many partitions? "))
	# initialize list with placeholder 0 index
	s = [0]
	for i in range(0, n):
		s.append(int(raw_input("enter a sequence value: ")))

	partition(s, n, k)

if __name__ == '__main__':
	main()


