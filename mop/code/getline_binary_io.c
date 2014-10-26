#define _GNU_SOURCE

#include <stdio.h>
#include <stdlib.h>

int main(void) {
	FILE* inputfile = fopen("input.txt", "r");
	if(!inputfile) {
		perror("fopen failed for inputfile:");
		exit(EXIT_FAILURE);
	}
	int numchars = 0;
	char* line = NULL;
	FILE* outputfile = fopen("output.txt", "w");
	if(!outputfile) {
		perror("fopen failed for outputfile:");
		fclose(inputfile);
		exit(EXIT_FAILURE);
	}
	while((numchars = getline(line, 1024, inputfile)) != -1) {
		fprintf(outputfile, "%d\n", numchars);
	}
	fclose(inputfile);
	fclose(outputfile);
	return EXIT_SUCCESS;
}
