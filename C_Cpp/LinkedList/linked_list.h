#pragma once
#include <stdio.h>
#include <stdlib.h>

typedef struct Node Node;

// Print the linkedlist.
void printLinkedList(Node* );
// Traverse the linkedlist
Node* traverseLinkedList(Node*, int );
// Insert a node
Node* insert(Node*, int , int );