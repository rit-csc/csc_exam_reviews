#include <stdlib.h>
#include <stdio.h>
#include <assert.h>

#define QUEUE_SZ 10

typedef struct queue {
	unsigned int size;
	void *contents[ QUEUE_SZ ];
} *QueueADT;

/* create, malloc and return a new queue */
QueueADT createQueue(void) {
	QueueADT q = (QueueADT)malloc(sizeof(struct queue));
	q->size = 0; /* initialize the queue's size to 0 */
	return q;
}

/* return whether or not the queue is empty based on its size */
int isEmpty(QueueADT q) {
	assert(q != NULL);
	return ( q->size == 0 );
}

/* push element onto end of the queue */
void enqueue(QueueADT q, void *data) {
	assert( q != NULL ); assert( q->size < QUEUE_SZ );
	q->contents[q->size++] = data;
	return;
}

/* remove and return the data of the first element of the queue */
void* dequeue(QueueADT q) {
	assert(q != NULL); assert(q->size > 0);
	void* ret = q->contents[0];
	q->size--;
	short int i = 0;
	while ( i < q->size ) {
		q->contents[i] = q->contents[i+1];
		++i;
	}
	return ret;
}

/* return the size of the queue */
unsigned int size(QueueADT q) {
	assert(q != NULL);
	return q->size;
}

