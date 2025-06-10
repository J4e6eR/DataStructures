# TODO: Implement a tree data structure Probably a binary tree data structure
import random
from Queue import Queue
class BSTNode:
  def __init__(self, data):
    self.left = None
    self.right = None
    self.data = data

  def __repr__(self):
    return f"BST NODE (Heigth: {calcHeight(self)}) -> {self.data}"

# Insertion would be done based on integer value whether its less than or greater than
def insert(rootNode: BSTNode, data: int):
  """
  newNode added in parameters for enabling recursion
  """

  if rootNode is None:
    rootNode = BSTNode(data)
  elif data <= rootNode.data:
    rootNode.left = insert(rootNode.left, data)
  else:
    rootNode.right = insert(rootNode.right, data)

  return rootNode

def DEBUG(data): print(data)

def BFSTraversal(rootNode: BSTNode, debug: bool = False, traversalQueue: Queue = None):
  """
  BFS traversal has only level-order
  """
  if rootNode == None:
    return
  if traversalQueue  is None:
    traversalQueue = Queue(rootNode)
  else:
    traversalQueue.append(rootNode)
  
  BFSTraversal(rootNode.left, True, traversalQueue)
  BFSTraversal(rootNode.right, True, traversalQueue)
  
  try:
    bstNode = traversalQueue.pop()
    if debug:
      DEBUG(bstNode.data)
  except AssertionError as e:
    pass 

def DFSTraversal(rootNode: BSTNode, technique: str):
  match technique:
    case 'in':
      # In-order
      pass
    case 'pre':
      # Pre-order
      pass
    case 'post':
      # Post order
      pass
    case _:
      print("No known DFS traversals.")

# Traversing the entire tree
def traversal(rootNode: BSTNode, traversalTechnique: str = "bfs", debug: bool = False):
  """
  As this is a non-linear data structure, it requires special traversal techniques like
  > Breadth First search.
    > level-order
  > Depth First Search
    > in-order   ->  <left subtree> <root> <right subtree>
    > pre-order  ->  <root> <left subtree> <right subtree>
    > post-order ->  <left subtree> <right subtree> <root>
  """
  match traversalTechnique:
    case 'bfs':
      BFSTraversal(rootNode, debug, None)
    case 'dfs':
      DFSTraversal(rootNode, 'in')
    case _:
      print("No known way to traverse.")


def calcHeight(rootNode: BSTNode):
  """
  <left node> <parent node> <right node> 
  parent node is the root node

  """

  # Base condition -> When we reach leaf node
  if rootNode.left == None or rootNode.right == None:
    return 0


  leftHeight = calcHeight(rootNode.left)
  rightHeight = calcHeight(rootNode.right)

  return max(leftHeight, rightHeight) + 1

if __name__ == "__main__":
  tree = BSTNode(567)
  for i in range(0, 100):
    number = random.randint(1, 100)
    insert(tree, number)
    print(f"Inserted {number}")

  # BFSTraversal(tree, True, None)
  BFSTraversal(tree, False, None)
