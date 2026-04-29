class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Insert function (for building BST)
def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

# Find minimum value node (used for deletion)
def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

# Delete function
def deleteNode(root, key):
    if root is None:
        return root

    # Step 1: Traverse to find the node
    if key < root.key:
        root.left = deleteNode(root.left, key)
    elif key > root.key:
        root.right = deleteNode(root.right, key)
    else:
        # Step 2: Node found
        # Case 1: No child
        if root.left is None and root.right is None:
            return None

        # Case 2: One child
        elif root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        # Case 3: Two children
        temp = minValueNode(root.right)
        root.key = temp.key
        root.right = deleteNode(root.right, temp.key)

    return root

# Inorder traversal (to check BST structure)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)

# Example usage
root = None
for val in [50, 30, 70, 20, 40, 60, 80]:
    root = insert(root, val)

print("Inorder before deletion:")
inorder(root)

root = deleteNode(root, 50)  # Delete root node

print("\nInorder after deleting 50:")
inorder(root)
