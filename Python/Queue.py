from linkedlist import Node, insert, delete, traverse

class Queue:
  # NOTE: We have to create the head node at the start while defining the Queue object
  def __init__(self, data):
    self.head = Node(data)
    self.tail = self.head

  def append(self, data):
    # NOTE: Hacking !!! to get the value added to the tail as the indexes are relative to the node passed.
    self.tail = insert(1, data, self.tail)
    # print("Tail while appending:", self.tail)
  
  def pop(self):
    # POP form head as QUEUE is a FIFO data structure
    deletedNode = delete(self.head, 0)
    assert deletedNode != None, "The queue is empty" 
    
    self.head.next = deletedNode.next
    return deletedNode

  def print(self): return traverse(self.head, True)
  def len(self): return traverse(self.head, False, True)



if __name__ == "__main__":
  queue = Queue(f"data_0")
  
  for i in range(1, 100):
    queue.append(f"data_{i}")
  
  print("After append")
  queue.print()

  for i in range(0, 20):
    queue.pop()

  print("After pop")
  queue.print()