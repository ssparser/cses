class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.key:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
        return root

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.key, end=" ")
        inorder_traversal(root.right)

def search(root, key):
    if root is None or root.key == key:
        return root
    if key < root.key:
        return search(root.left, key)
    return search(root.right, key)

def min_value_node(node):
    current = node
    while(current.left is not None):
        current = current.left
    return current

def delete_node(root, key):
    if root is None:
        return root

    if key < root.key:
        root.left = delete_node(root.left, key)
    elif key > root.key:
        root.right = delete_node(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = min_value_node(root.right)
        root.key = temp.key
        root.right = delete_node(root.right, temp.key)

    return root

if __name__ == '__main__':
    root = None
    root = insert(root, 50)
    root = insert(root, 30)
    root = insert(root, 20)
    root = insert(root, 40)
    root = insert(root, 70)
    root = insert(root, 60)
    root = insert(root, 80)

    print("Inorder traversal of the given tree")
    inorder_traversal(root)
    print("\n")

    key = 60
    if search(root, key) is not None:
        print(f"{key} found in the BST")
    else:
        print(f"{key} not found in the BST")

    root = delete_node(root, 20)
    print("Inorder traversal after deleting 20")
    inorder_traversal(root)
    print("\n")