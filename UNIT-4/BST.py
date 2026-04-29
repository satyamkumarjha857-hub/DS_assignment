class BSTNODE:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
    
def insert(root,key):
    if root is None:
        return BSTNODE(key)
    if key < root.key:
        root.left = insert(root.left,key)
    elif key > root.key:
        root.right = insert(root.right,key)
    return root

def search(root , key):
    if root is None:
        return False
    if root.key == key:
        return True
    if key < root.key:
        return search(root.left,key)
    return search(root.right,key)

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.key, end=" ")
    inorder(root.right)

root = None

for values in [50,30,70,20,40,60,80]:
    root = insert(root,values)

print("Inorder traversal of BST:")
inorder(root)
print()

print("Is 40 present?:", search(root,40))  # True
print("Is 90 present?:", search(root,90))  # False