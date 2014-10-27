#define _GNU_SOURCE

#include <stdio.h>
#include <stdlib.h>

int main(void) {
	FILE* inputfile = fopen("input.txt", "r");
	if(!inputfile) {
		perror("fopen failed for inputfile:");
		exit(EXIT_FAILURE);
	}
	ssize_t numchars = 0;
	char* line = NULL;
	FILE* outputfile = fopen("output.txt", "wb");
	if(!outputfile) {
		perror("fopen failed for outputfile:");
		fclose(inputfile);
		exit(EXIT_FAILURE);
	}
	size_t n = 0;
	while((numchars = getline(&line, &n, inputfile)) != -1) {
		int towrite[1] = { numchars };
		if(fwrite((void*)towrite, sizeof(int), 1, outputfile) != 1) {
			perror("fwrite into outputfile failed:");
			fclose(inputfile);
			fclose(outputfile);
			exit(EXIT_FAILURE);
		}
	}
	free(line);
	fflush(outputfile);
	fclose(inputfile);
	fclose(outputfile);
	return EXIT_SUCCESS;
}
