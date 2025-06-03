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
};

void printLinkedList(Node* head){
    int i = 0;
    while(head->next == NULL){
        printf("%d -> %d\n", i, head->data);
        i++;
        head = head->next;
    }
}

Node* traverseLinkedList(Node* head, int index){
    int i = 0;
    while(head->next == NULL){
        if (i == index){
            return head;
        }
        i++;
        head = head->next;
    }
    return NULL;
}


Node* insert(Node* head, int data, int index){
    // Returns the node
    Node* newNode = new Node(); 
    newNode -> data = data;
    if (index == 0 && head == NULL){
        // This represents the head
        newNode->next = NULL;
    }


    
}

int main(){
    Node* head = new Node(0);

}