from linkedlist import Node, insert, delete

# TODO: Build a queue on top of linked list
class Queue:
  # NOTE: We have to create the head node at the start while defining the Queue object
  def __init__(self, data):
    self.head = Node(data)
    self.tail = self.head

  def append(self, data):
    # NOTE: Hacking !!! to get the value added to the tail as the indexes are relative to the node passed.
    self.tail = insert(1, data, self.tail)
  
  def pop(self):
    # POP form head as QUEUE is a FIFO data structure
    deletedNode = delete(self.head, 0)
    assert deletedNode == None, "The queue is empty" 
    self.head = deletedNode.next



if __name__ == "__main__":
  pass