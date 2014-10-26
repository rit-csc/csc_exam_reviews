
#include <stdio.h>
#include <stdlib.h>

typedef struct Node 
{
	void* data;
	struct Node* next;
} Node;

#define _NODE_IMPL_
#include "node.h"

Node* createNode(void* data)
{
	Node* n = (Node*)malloc(sizeof(Node));
	n->data = data;
	n->next = '\0';
	return n;
}

int main()
{
	Node* n = createNode((void*)123);
	printf("%d\n", (int)(n->data));
	return 0;
}

