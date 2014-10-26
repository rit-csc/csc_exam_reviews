
#ifndef _NODE_IMPL_
typedef struct { } *Node;
#endif

Node createNode(void* data);
Node getNext(Node n);
