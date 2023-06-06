class Node:
    def __init__(self):
        self.data = None
        self.leftch = None
        self.rightch = None
        self.leftTh = False
        self.rightTh = False
        self.next = None
        self.prev = None

def insert(root, key, prev_node=None):
    if root is None:
        root = Node()
        root.data = key
        root.prev = prev_node 
    elif key < root.data:
        root.leftch = insert(root.leftch, key, root)
        if root.leftch.next is None:
            root.leftch.next = root
            root.leftch.prev = root.prev
            if root.prev is not None:
                root.prev.next = root.leftch
            root.prev = root.leftch
    else:
        root.rightch = insert(root.rightch, key, root)
        if root.rightch.prev is None:
            root.rightch.prev = root
            root.rightch.next = root.next
            if root.next is not None:
               root.next.prev = root.rightch
            root.next = root.rightch
    return root

def search(root, key):
    if root is None:
        return None
    elif root.data == key:
        return root
    elif key < root.data:
        if isinstance(root.leftch, Node) and root.leftch is not None:
            return search(root.leftch, key)
        else:
            return None
    else:
        if isinstance(root.rightch, Node) and root.rightch is not None:
            return search(root.rightch, key)
        else:
            return None


def inorder(root):
    if root:
        inorder(root.leftch)
        print(root.data, end=" ")
        inorder(root.rightch)

def delete(root, key):
    if root is None:
        return root

    if key < root.data:
        root.leftch = delete(root.leftch, key)
    elif key > root.data:
        root.rightch = delete(root.rightch, key)
    else:
        if root.leftch is None and root.rightch is None:
            root = None
        elif root.leftch is None:
            root = root.rightch
        elif root.rightch is None:
            root = root.leftch
        else:
            min_value = find_min_value(root.rightch)
            root.data = min_value
            root.rightch = delete(root.rightch, min_value)

    return root

def find_min_value(root):
    current = root
    while current.leftch is not None:
        current = current.leftch
    return current.data

def postorder(root):
    if root:
        postorder(root.leftch)
        postorder(root.rightch)
        print(root.data, end=" ")

def traverse_postorder(root):
    print("Postorder traversal:")
    postorder(root)
    print()

def preorder(root):
    if root:
        print(root.data, end=" ") 
        preorder(root.leftch)      
        preorder(root.rightch)    

def traverse_preorder(root):
    print("Preorder traversal:")
    preorder(root)
    print()

def main():
    root = None

    while True:
        print(" 1. Add node\n 2. Delete the node\n 3. Search\n 4. Order\n 5. Postorder\n 6. Preorder\n 7. Exit")
        choice = int(input("Please enter a number: "))

        if choice == 1:
            insert_choice = input("Do you want to enter the node manually or from a file? (m/f): ")
            if insert_choice.lower() == "m":
                key = int(input("Please enter the desired number: "))
                root = insert(root, key)
                print("Node added successfully.")
            elif insert_choice.lower() == "f":
                filename = input("Please enter the file name: ")
                try:
                    with open(filename, 'r') as file:
                        numbers = file.readline().split()
                        for number in numbers:
                            key = int(number.strip())
                            root = insert(root, key)
                        print("Nodes added successfully from the file.")
                except FileNotFoundError:
                    print("File not found. Please make sure the file exists.")
            else:
                print("Invalid choice. Please try again.")

        elif choice == 2:
            key = int(input("Please enter the desired number to delete: "))
            deleted_node = delete(root, key)
            if deleted_node is not None:
                print("Node with value", deleted_node.data, "deleted successfully.")
            else:
                print("Node with value", key, "could not be found and deleted.")

        elif choice == 3:
            key = int(input("Please enter the desired number to search: "))
            result = search(root, key)
            if result is not None:
                print("Node with value", result.data, "found.")
            else:
                print("Node with value", key, "not found.")

        elif choice == 4:
            print("In-order traversal:")
            inorder(root)

        elif choice == 5:
            traverse_postorder(root)

        elif choice == 6:
            traverse_preorder(root)

        elif choice == 7:
            print("Hope to see you again!")
            break

        print('\n')
        print("*" * 100)
main()




