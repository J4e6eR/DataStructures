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



# Traversing the entire tree
def traversal(rootNode: BSTNode, traversalTechnique: str = "bfs", technique: str = 'level', debug: bool = False):
  """
  As this is a non-linear data structure, it requires special traversal techniques like
  > Breadth First search.
    > level-order
  > Depth First Search
    > in-order   ->  <left subtree> <root> <right subtree>
    > pre-order  ->  <root> <left subtree> <right subtree>
    > post-order ->  <left subtree> <right subtree> <root>
  """

  def _BFSTraversal(rootNode: BSTNode, debug: bool = False, traversalQueue: Queue = None):
    """
    BFS traversal has only level-order
    """
    if rootNode == None:
      return
    
    if traversalQueue is None:
      traversalQueue = Queue(rootNode)
    
    if traversalQueue is not None:
      # Prevents adding the root node twice in the queue, especially while creating it.
      traversalQueue.append(rootNode)
    
    _BFSTraversal(rootNode.left, True, traversalQueue)
    _BFSTraversal(rootNode.right, True, traversalQueue)
    
    try:
      bstNode = traversalQueue.pop()
      if debug:
        DEBUG(bstNode.data)
    except AssertionError as e:
      pass 
    
  def _DFSTraversal(rootNode: BSTNode, technique: str = 'pre', debug: bool = False):

    # in-order   ->  <left subtree> <root> <right subtree>
    def _inorder(rootNode: BSTNode, debug: bool = False):
      if rootNode == None:
        return
      _inorder(rootNode.left, debug)
      DEBUG(rootNode)
      _inorder(rootNode.right, debug)

    # pre-order  ->  <root> <left subtree> <right subtree>
    def _preorder(rootNode: BSTNode, debug: bool  = False):
      if rootNode == None:
        return
      DEBUG(rootNode)
      _preorder(rootNode.left, debug)
      _preorder(rootNode.right)

    # post-order ->  <left subtree> <right subtree> <root>
    def _postorder(rootNode: BSTNode, debug: bool = False):
      if rootNode == None:
        return
      _postorder(rootNode.left, debug)
      _postorder(rootNode.right, debug)
      DEBUG(rootNode)

    match technique:
      case 'in':
        # In-order
        _inorder(rootNode, debug)
        pass
      case 'pre':
        # Pre-order
        _preorder(rootNode, debug)
        pass
      case 'post':
        # Post order
        _postorder(rootNode, debug)
        pass
      case _:
        print("No known DFS traversals.")
  
  
  match traversalTechnique:
    case 'bfs':
      _BFSTraversal(rootNode, debug, None)
    case 'dfs':
      _DFSTraversal(rootNode, technique)
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
  tree = BSTNode(10)
  for i in range(0, 100):
    number = random.randint(1, 100)
    insert(tree, number)
    print(f"Inserted {number}")

  # BFSTraversal(tree, True, None)
  traversal(tree, 'dfs', 'in', True)
