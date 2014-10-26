
#include <stdlib.h>
#include <stdio.h>
#include <assert.h>
#include "node.h"

typedef struct queue
{
	unsigned int size;
	Node front;
} *QueueADT;

int isEmpty(QueueADT q)
{
	assert(q != NULL);
	return ( q->size == 0 );
}

void enqueue(QueueADT q, Node n)
{
	// TODO
	return;
}

Node dequeue(QueueADT q)
{
	assert(q->size > 0);
	q->size--;
	/* free node */
	Node ret = q->front;
	q->front = getNext(q->front);
	return ret;
}

unsigned int size(QueueADT q)
{
	assert(q != NULL);
	return q->size;
}

// for testing, should be removed in final build
int main()
{
	return EXIT_SUCCESS;
}
