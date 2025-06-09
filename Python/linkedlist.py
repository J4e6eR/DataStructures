class Node:
  def __init__(self, data, head:bool = False):
    self.data = data
    self.next = None
    self.prev = None

  def __repr__(self):
    return f"Node Val: {self.data}"


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

def readNode(headNode: Node, index: int):
  position = 0

  while (headNode != None):
    if position == index:
      return headNode
    position += 1
    headNode = headNode.next
  
  # If index is much bigger than the actual size
  return None

def delete(headNode: Node, index: int):
  """
  head -> node 1 -> node 2
  case 1: head delete
    [del] -> node 1 -> node 2
  case 2: tail delete
    head -> node 1 -> [del]
  case 3: Any other index
    head -> [del] -> node 2
  """
  
  if index == 0:
    # Head node 
    head = headNode.next
    head.prev = None 
    return head

  toDelNode = readNode(headNode, index)
  if toDelNode is not None:
    prevNode = toDelNode.prev
    nextNode = toDelNode.next
    
    prevNode.next = nextNode
    nextNode.prev = prevNode
  
  return toDelNode



# Traverse through the entire linkedlist
def traverse(headNode, print_node:bool = False, len: bool = False):
  position = 0
  
  while (headNode != None):
    if print_node:
      print(f"Node ({position})-> {headNode.data}")
    position += 1
    headNode = headNode.next
  
  if len: return position


# Length of the linkedlist
def len(headNode: Node): return traverse(headNode, print_node = False, len=True)

if __name__ == "__main__":
  head = Node(b"hello")
  for i in range (0, 100):
    if i == 0:
      head = insert(i, f"data_{i}".encode('utf-8'), head)
    else:
      _head = insert(i, f"data_{i}".encode('utf-8'), head)
  
  # head = _head if _head is not None else head
  # traverse(head, True)

  print(f"Length of node: {len(head)}")

  head = delete(head, 0)
  print("The deleted node:", head)
  # print("Head node:", readNode(head, 0))
  traverse(head, print_node=True)
  
