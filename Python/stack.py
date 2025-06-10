# Stack data sturucture is a First In Last Out Data structure
from linkedlist import Node, insert, delete, traverse

class Stack:
  # NOTE: We have to create the head node at the start while defining the Queue object
  def __init__(self, data):
    self.head = Node(data)
    self.tail = self.head

  def append(self, data):
    # NOTE: Hacking !!! 1 is added to get the value added to the tail as the indexes are relative to the node passed.
    self.tail = insert(1, data, self.tail)
  
  def pop(self):
    # POP form tail as Stack is a FILO data structure
    print("Tail before deletion:", self.tail)
    deletedNode = delete(self.tail, 0, tail=True)
    assert deletedNode != None, "The stack is empty" 
    print("Tail after deletion:", self.tail)
    self.tail.prev = deletedNode.prev
    return deletedNode

  def print(self): return traverse(self.head, True)
  def len(self): return traverse(self.head, False, True)



if __name__ == "__main__":
  stack = Stack(f"data_0")
  
  for i in range(1, 100):
    stack.append(f"data_{i}")
  
  print("After append")
  stack.print()

  for i in range(0, 20):
    print("Deleted node: ", stack.pop().data)

  print("After pop")
  stack.print()