class Node:
  def __init__(self, data, head:bool = False):
    self.data = data
    self.next = None
    self.prev = None


# Insert the data at a particular index
def insert(index, data, curNode: Node):
  """
                  newNode
  head --> node 1  --> node 2 --> newNode
  |         prevNode  |  nextNode    
  """

  def _insert(newNode: Node, prevNode: Node, nextNode: Node):
    # New node manage
    newNode.next = nextNode
    newNode.prev = prevNode

    if prevNode != None: prevNode.next = newNode # Represents the head node
    if nextNode != None: nextNode.prev = newNode # Represents the tail node

  newNode = Node(data)
  headNode = newNode
  # Its a head
  if index == 0:
      _insert(newNode, None, curNode.next)
      return headNode
    
  position = 0
  while(curNode != None):
    if position + 1 == index:
      _insert(newNode, curNode, curNode.next)
    
    position += 1
    curNode = curNode.next  

  return None

def traverse(headNode, print:bool = False):
  position = 0
  
  while (headNode != None):
    if print:
      print(f"Node ({position})-> {headNode.data}")
    position += 1
    headNode = headNode.next
  
  return position 

# Length of the linkedlist
def len(headNode: Node): return traverse(headNode, False)


if __name__ == "__main__":
  head = Node(b"hello")
  for i in range (0, 100):
    _head = insert(i, f"data_{i}".encode('utf-8'), head)
  
  head = _head if _head is not None else head
  traverse(head)

  print(f"Length of node: {len(head)}")
  
