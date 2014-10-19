// Calculates the Edit Distance between two strings. Adapted from the
// Algorithm Design Manual by Steven Skiena

#include <string.h>
#include <stdio.h>

#define BUFSIZE 24
#define MATCH	0
#define	INSERT	1
#define	DELETE	2

int matrix[BUFSIZE][BUFSIZE];

// replaces the '\n' at the end of str with '\0' if it exists	
void newline_to_terminator(char *str) {
	char *pos;
	if ((pos=strchr(str, '\n')) != NULL)
	    *pos = '\0';
}

// initializes zeroth row of the matrix at column i
void row_init(int i) {
	matrix[0][i] = i;
}

// initializes the zeroth column of the matrix at row i
void column_init(int i) {
	matrix[i][0] = i;
}

// returns 0 if a == b, otherwise 1
int match(char a, char b) {
	if (a == b) {
		return 0;
	}
	return 1;
}

int string_compare(char *str1, char *str2) {
	int i, j, k;
	int opt[3];

	// initialize the lookup table's 0 row and column
	for (i = 0; i < BUFSIZE; i++) {
		row_init(i);
		column_init(i);
	}

	// build up the matrix
	for (i = 1; i < strlen(str1); i++) {
		for (j = 1; j < strlen(str2); j++) {
			opt[MATCH] = matrix[i-1][j-1] + match(str1[i], str2[j]);
			opt[INSERT] = matrix[i][j-1] + 1;
			opt[DELETE] = matrix[i-1][j] + 1;

			matrix[i][j] = opt[MATCH];
			for (k = INSERT; k <= DELETE; k++) {
				if (opt[k] < matrix[i][j]) {
					matrix[i][j] = opt[k];
				}
			}
		}
	}

	// return the edit distance
	return matrix[strlen(str1)-1][strlen(str2)-1];
}

int main(int argc, char **argv) {
	char str1[BUFSIZE];
	char str2[BUFSIZE];
	int distance;

	printf("Enter two strings to calculate the edit distance between\n");
	printf("String one: ");
	fgets(&str1[1], BUFSIZE - 1, stdin);
	printf("String two: ");
	fgets(&str2[1], BUFSIZE - 1, stdin);

	// replace trailing newlines with string terminators
	newline_to_terminator(str1);
	newline_to_terminator(str2);

	int distance = string_compare(str1, str2);

	printf("The edit distance between %s and %s is %d\n", 
		str1, str2, distance);
}

