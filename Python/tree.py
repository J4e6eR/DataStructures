# TODO: Implement a tree data structure Probably a binary tree data structure
import random
class BSTNode:
  def __init__(self, data):
    self.left = None
    self.right = None
    self.data = data


# Insertion would be done based on integer value whether its less than or greater than
def insert(rootNode: BSTNode, data: int, newNode: BSTNode = None):
  """
  newNode added in parameters for enabling recursion
  """
  if newNode is None:
    newNode = BSTNode(data)
  else:
    # Currently the new node is added just to the root node
    # TODO: What to do if the height of the tree is more than 1
    # TODO: Traverse to the appropriate node and then insert, which includes traversal techniques.
    # TODO: Learn self-balancing binary search trees (namely AVL Trees)
    if newNode.data <= rootNode.data:
      rootNode.left = insert(rootNode.left, data, newNode)
    elif newNode.data > rootNode.data:
      rootNode.right = insert(rootNode.right, data, newNode)
    
    return rootNode

def BFSTraversal(rootNode: BSTNode, debug: bool = False):
  pass

def DFSTraversal(rootNode: BSTNode, technique: str):
  pass

# Trsversing the entire tree
def traversal(rootNode: BSTNode, traversalTechnique: str = "bfs"):
  """
  As this is a non-linear data structure, it requires special traversal techniques like
  > Breadth First search.
    > level-order
  > Depth First Search
    > in-order   ->  <left subtree> <root> <right subtree>
    > pre-order  ->  <root> <left subtree> <right subtree>
    > post-order ->  <left subtree> <right subtree> <root>
  """
  


  pass


if __name__ == "__main__":
  tree = BSTNode(5)
  for i in range(0, 100):
    number = random.randint(1, 100)
    insert(tree, number)
    print(f"Inserted {number}")
