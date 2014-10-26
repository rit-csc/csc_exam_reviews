#include <stdio.h>

#ifdef WINDOWS
#include <windows.h>

#define WIN_CREATEFILE(a) CreateFile(a, \
									GENERIC_READ, \
									FILE_SHARE_READ, \
									OPEN_ALWAYS, \
									FILE_ATTRIBUTE_NORMAL)
#endif

int main(int argc, char** argv) {
	// ... some previous initialization stuff

#ifdef WINDOWS
	HANDLE file = WIN_CREATEFILE(argv[1]); 
#else
	FILE* file = fopen(argv[1], "r");
#endif

	// ... do some more stuff

	return 0;
}
