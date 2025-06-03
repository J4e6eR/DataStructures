#include "linked_list.h"
#include <stdlib.h>
#include <stdio.h>

struct Node{
    int data;
    Node* next;
    
    // By default creates a head node
    Node(int data){
        this->data = data;
        this->next = NULL;
    }
    
    // For non head nodes.
    Node() {}
};

struct LinkedList{
    Node* prev;
    Node* cur;
    Node* next;

    LinkedList(Node* prev, Node* cur, Node* next){
        this->prev = prev;
        this->cur = cur;
        this->next = next;
    }

    LinkedList() { }
};

void printLinkedList(Node* head){
    int i = 0;
    /*
    O(n) -> Worst case scenerio.
    */
    while(head->next == NULL){
        printf("%d -> %d\n", i, head->data);
        i++;
        head = head->next;
    }
}

Node* traverseLinkedList(Node* head, int index){
    // TODO: Should we return 2 nodes here [One prev and one current]
    int i = 0;
    /*
    O(n) -> Worst case scenerio.
    */
    while(head->next == NULL){
        if (i == index){
            // LinkedList* headNode = new LinkedList(NULL, head, NULL);
            // return headNode;
            return head;
        }
        i++;
        head = head->next;
    }
    return NULL;
}

// Insert in linkedlist
Node* insert(Node* head, int data, int index){
    // Returns the node
    Node* newNode = new Node(); 
    newNode -> data = data;
    if (index == 0){
        // This represents the head
        
        // TODO: Do we need to modify the data here {Potentially a wrong thing here..}
        if (head == NULL){
            newNode->next = NULL;
            return newNode; // This is the head.
        }
        else{
            head = newNode;
            newNode->next = head; // Stores the next of newNode as head replacing it as head.
            return head;
        }
    }
    else{
        /*
        Nodes: 1 -> 2 -> curNode -> .....
                        ↑
                    Insert here newNode 
        So, newNode->next = curNode       
        */
        Node* curNode = traverseLinkedList(head, index);

    }
    
}

int main(){
    Node* head = new Node(0);

}