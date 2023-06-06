import tkinter as tk
from tkinter import messagebox

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
            return []

        traversal = [root.data]
        if not root.leftTh:
            traversal.extend(self.preorder(root.leftch))
        if not root.rightTh:
            traversal.extend(self.preorder(root.rightch))

        return traversal

    def postorder(self, root):
        if root is None:
            return []

        traversal = []
        if not root.leftTh:
            traversal.extend(self.postorder(root.leftch))
        if not root.rightTh:
            traversal.extend(self.postorder(root.rightch))
        traversal.append(root.data)

        return traversal

    def inorder(self, root):
        if root is None:
            return []

        traversal = []
        if not root.leftTh:
            traversal.extend(self.inorder(root.leftch))
        traversal.append(root.data)
        if not root.rightTh:
            traversal.extend(self.inorder(root.rightch))

        return traversal

    def search(self, root, key):
        if root is None:
            return None
        elif root.data == key:
            return root
        elif key < root.data:
            if isinstance(root.leftch, Node) and root.leftch is not None:
                return self.search(root.leftch, key)
            else:
                return None
        else:
            if isinstance(root.rightch, Node) and root.rightch is not None:
                return self.search(root.rightch, key)
            else:
                return None


class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Threaded Binary Tree")
        self.geometry("400x300")

        self.tree = ThreadedBinaryTree()

        self.input_label = tk.Label(self, text="Enter a number:")
        self.input_label.pack()

        self.input_entry = tk.Entry(self)
        self.input_entry.pack()

        self.add_button = tk.Button(self, text="Add Node", command=self.add_node)
        self.add_button.pack()

        self.delete_button = tk.Button(self, text="Delete Node", command=self.delete_node)
        self.delete_button.pack()

        self.search_button = tk.Button(self, text="Search Node", command=self.search_node)
        self.search_button.pack()

        self.inorder_button = tk.Button(self, text="Inorder Traversal", command=self.inorder_traversal)
        self.inorder_button.pack()

        self.postorder_button = tk.Button(self, text="Postorder Traversal", command=self.postorder_traversal)
        self.postorder_button.pack()

        self.preorder_button = tk.Button(self, text="Preorder Traversal", command=self.preorder_traversal)
        self.preorder_button.pack()

        self.exit_button = tk.Button(self, text="Exit", command=self.quit)
        self.exit_button.pack()

    def add_node(self):
        try:
            key = int(self.input_entry.get())
            self.tree.insert(key)
            messagebox.showinfo("Node Added", "Node added successfully.")
            self.input_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid integer.")

    def delete_node(self):
        try:
            key = int(self.input_entry.get())
            self.tree.delete(key)
            messagebox.showinfo("Node Deleted", "Node deleted successfully.")
            self.input_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid integer.")

    def search_node(self):
        try:
            key = int(self.input_entry.get())
            if self.tree.search(self.tree.root.leftch, key):
                messagebox.showinfo("Node Found", "Node found.")
            else:
                messagebox.showinfo("Node Not Found", "Node not found.")
            self.input_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid integer.")

    def inorder_traversal(self):
        traversal = self.tree.inorder(self.tree.root.leftch)
        messagebox.showinfo("Inorder Traversal", " ".join(str(node) for node in traversal))

    def postorder_traversal(self):
        traversal = self.tree.postorder(self.tree.root.leftch)
        messagebox.showinfo("Postorder Traversal", " ".join(str(node) for node in traversal))

    def preorder_traversal(self):
        traversal = self.tree.preorder(self.tree.root.leftch)
        messagebox.showinfo("Preorder Traversal", " ".join(str(node) for node in traversal))


if __name__ == "__main__":
    app = Application()
    app.mainloop()
