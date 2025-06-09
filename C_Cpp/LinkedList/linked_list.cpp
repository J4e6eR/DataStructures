#include "linked_list.h"
#include <stdlib.h>
#include <stdio.h>

struct Node{
    int data;
    Node* prev = nullptr;
    Node* next = nullptr;
    
    // By default creates a head node
    Node(int data){
        this->data = data;
        this->next = nullptr;
        this->prev= nullptr;
    }
    
    // For non head nodes.
    Node() {}

    ~Node(){
        free(this);
    }
};

// struct LinkedList{
//     Node* prev;
//     Node* cur;
//     Node* next;

//     LinkedList(Node* prev, Node* cur, Node* next){
//         this->prev = prev;
//         this->cur = cur;
//         this->next = next;
//     }

//     LinkedList() { }
// };

void printLinkedList(Node* head){
    int i = 1; // i = 0 we are manually printing
    /*
    O(n) -> Worst case scenerio.
    */
    printf("Head (Index = 0) -> %d\n", head->data);
    while(head->next != nullptr){
        printf("(Index = %d )-> %d\n", i, head->data);
        i++;
        head = head->next;
    }
}

Node* traverseLinkedList(Node* head, int index){
    // TODO: Should we return 2 nodes here [One prev and one current]
    int i = 0;
    if (head == nullptr) {
        return nullptr; // Handle empty list
    }
    /*
    O(n) -> Worst case scenerio.
    */
    while(head->next != nullptr){
        printf("i in traversed list: %d\n", i);
        // printf("index in traversed list: %d\n", index);
        if (i == index){
            printf("INdex found %d\n", index);
            // LinkedList* headNode = new LinkedList(NULL, head, NULL);
            // return headNode;
            return head;
        }
        i++;
        head = head->next;
    }
    // return head; // Always get the last element in the linked list.
    return nullptr;
}

// Insert in linkedlist
Node* insert(Node* head, int data, int index){
    // Returns the node
    Node* newNode = new Node(); 
    newNode -> data = data;
    printf("New node to be inserted: %d\n", newNode->data);
    
    // The head node.
    if (index == 0) {
        // This represents the head
        if (head != nullptr){
            newNode->next = head;
            head->prev = newNode;
        }
        // head = newNode;
        return newNode;
    }

    /*
    1 -> 2 -> prevNode -> curNode -> nextNode
                        ↑
                    Insert here {newNode}
    */
    
    Node* curNode = traverseLinkedList(head, index);
    if (curNode != nullptr){
        Node* prevNode = curNode->prev;
        prevNode->next = newNode;

        newNode->next = curNode;
        newNode->prev = prevNode;

        curNode->prev = newNode;
        
    }
    return newNode;
}

int main(){
    Node* head = new Node(50);
    printLinkedList(head);
    // Node* currentNode = traverseLinkedList(head, 0);  
    // printf("Current node: %d\n", currentNode->data); 
    
    Node* insertedNode = insert(head, 100, 0);
    printLinkedList(insertedNode);
    // Node* insertedNode = insert(head, 100, 1);
    // printf("Inserted node data= %d\n", insertedNode->data);
    // insertedNode = insert(head, 200, 2);
    // insertedNode = insert(head, 300, 3);
    // printLinkedList(head);
}