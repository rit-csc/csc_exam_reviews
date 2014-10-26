
#include <stdio.h>
#include <stdlib.h>

typedef struct Node 
{
	void* data;
	struct Node* next;
} Node;

#define _NODE_IMPL_

Node* createNode(void* data)
{
	Node* n = (Node*)malloc(sizeof(Node));
	n->data = data;
	n->next = '\0';
	return n;
}

