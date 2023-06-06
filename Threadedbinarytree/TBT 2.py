class Node:
    def __init__(self, data=None):
        self.data = data
        self.leftch = None
        self.rightch = None
        self.leftTh = False
        self.rightTh = False


class ThreadedBinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, d):
        if self.root is None:
            self.root = Node()
            self.root.rightch = self.root.leftch = self.root
            self.root.leftTh = True
            self.root.data = float("inf")

        cur = self.root
        while True:
            if cur.data < d:
                if cur.rightTh:
                    break
                cur = cur.rightch
            elif cur.data > d:
                if cur.leftTh:
                    break
                cur = cur.leftch
            else:
                return
        temp = Node()
        temp.data = d
        temp.rightTh = temp.leftTh = True
        if cur.data < d:
            temp.rightch = cur.rightch
            temp.leftch = cur
            cur.rightch = temp
            cur.rightTh = False
        else:
            temp.rightch = cur
            temp.leftch = cur.leftch
            cur.leftch = temp
            cur.leftTh = False

    def delete(self, d):
        dest = self.root.leftch
        cur = self.root
        while True:
            if dest.data < d:
                if dest.rightTh:
                    return
                cur = dest
                dest = dest.rightch
            elif dest.data > d:
                if dest.leftTh:
                    return
                cur = dest
                dest = dest.leftch
            else:
                break
        target = dest
        if not dest.rightTh and not dest.leftTh:
            cur = dest
            target = dest.leftch
            while not target.rightTh:
                cur = target
                target = target.rightch
            dest.data = target.data

        if cur.data >= target.data:
            if target.rightTh and target.leftTh:
                cur.leftch = target.leftch
                cur.leftTh = True
            elif target.rightTh:
                largest = target.leftch
                while not largest.rightTh:
                    largest = largest.rightch
                largest.rightch = cur
                cur.leftch = target.leftch
            else:
                smallest = target.rightch
                while not smallest.leftTh:
                    smallest = smallest.leftch
                smallest.leftch = target.leftch
                cur.leftch = target.rightch
        else:
            if target.rightTh and target.leftTh:
                cur.rightch = target.rightch
                cur.rightTh = True
            elif target.rightTh:
                largest = target.leftch
                while not largest.rightTh:
                    largest = largest.rightch
                largest.rightch = target.rightch
                cur.rightch = target.leftch
            else:
                smallest = target.rightch
                while not smallest.leftTh:
                    smallest = smallest.leftch
                smallest.leftch = cur
                cur.rightch = target.rightch

    def preorder(self, root):
        if root is None:
            return

        print(root.data, end=" ")
        if not root.leftTh:
            self.preorder(root.leftch)
        if not root.rightTh:
            self.preorder(root.rightch)

    def postorder(self, root):
        if root is None:
            return

        if not root.leftTh:
            self.postorder(root.leftch)
        if not root.rightTh:
            self.postorder(root.rightch)
        print(root.data, end=" ")

    def inorder(self, root):
        if root is None:
            return

        if not root.leftTh:
            self.inorder(root.leftch)
        print(root.data, end=" ")
        if not root.rightTh:
            self.inorder(root.rightch)

    def search(self, root, key):
        if root is None:
            return None
        elif root.data == key:
            return root
        elif key < root.data and not root.leftTh:
            return self.search(root.leftch, key)
        elif key > root.data and not root.rightTh:
            return self.search(root.rightch, key)
        else:
            return None



def main():
    tbt = ThreadedBinaryTree()

    while True:
        print(" 1. Add node\n 2. Delete the node\n 3. Search\n 4. Inorder\n 5. Postorder\n 6. Preorder\n 7. Exit")
        choice = int(input("Please enter a number: "))

        if choice == 1:
            insert_choice = input("Do you want to enter the node manually or from a file? (m/f): ")
            if insert_choice.lower() == "m":
                key = int(input("Please enter the desired number: "))
                tbt.insert(key)
                print("Node added successfully.")
            elif insert_choice.lower() == "f":
                filename = input("Please enter the file name: ")
                try:
                    with open(filename, 'r') as file:
                        numbers = file.readline().split()
                        for number in numbers:
                            key = int(number.strip())
                            tbt.insert(key)
                        print("Nodes added successfully from the file.")
                except FileNotFoundError:
                    print("File not found. Please make sure the file exists.")
            else:
                print("Invalid choice. Please try again.")

        elif choice == 2:
            key = int(input("Please enter the desired number to delete: "))
            tbt.delete(key)

        elif choice == 3:
            key = int(input("Please enter the desired number to search: "))
            if tbt.search(tbt.root.leftch, key):
                print("found.")
            else:
                print("Not found.")

        elif choice == 4:
            print("Inorder traversal:")
            tbt.inorder(tbt.root.leftch)

        elif choice == 5:
            print("Postorder traversal:")
            tbt.postorder(tbt.root.leftch)

        elif choice == 6:
            print("Preorder traversal:")
            tbt.preorder(tbt.root.leftch)

        elif choice == 7:
            print("Hope to see you again!")
            break

        print('\n')
        print("*" * 100)


if __name__ == "__main__":
    main()
