
#include <stdlib.h>
#include <stdio.h>
#include "node.h"

typedef struct queue
{
	unsigned int size;
	Node* front;
} QueueADT;

int isEmpty(q)
QueueADT q;
{
	// TODO
	return 0;
}

void enqueue(q, n)
QueueADT q;
Node n;
{
	return;
}

Node dequeue(q)
QueueADT q;
{
	return '\0';
}

unsigned int size(q)
QueueADT q;
{
	return -1;
}

// for testing, should be removed in final build
int main()
{
	return EXIT_SUCCESS;
}