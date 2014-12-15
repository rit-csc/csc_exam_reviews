#include <fcntl.h>
#include <unistd.h>
#include <string.h>

int main(void) {
    char buffer[30]; // number of characters in file + 1
    int fd = open("sliding.txt", O_RDWR);
    read(fd, buffer, 29);
    buffer[29] = '\0'; // for use in string functions
    char* modifiedLocation = strstr(buffer, "^<<<<");
    int offset = modifiedLocation - buffer;
    lseek(fd, offset, SEEK_SET);
    write(fd, ">>>>v", 5);
    close(fd);
    return 0;
}
