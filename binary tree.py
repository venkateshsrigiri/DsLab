Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
...         self.right = None
... 
... class BinaryTree:
...     def __init__(self):
...         self.root = None
... 
...     def insert(self, data):
...         new_node = Node(data)
...         if self.root is None:
...             self.root = new_node
...         else:
...             temp = self.root
...             while True:
...                 if data < temp.data:
...                     if temp.left is None:
...                         temp.left = new_node
...                         break
...                     else:
...                         temp = temp.left
...                 else:
...                     if temp.right is None:
...                         temp.right = new_node
...                         break
...                     else:
...                         temp = temp.right
... 
...     def search(self, data):
...         temp = self.root
...         while temp is not None:
...             if temp.data == data:
...                 return True
...             elif data < temp.data:
...                 temp = temp.left
...             else:
...                 temp = temp.right
...         return False
... 
...     def delete(self, data):
...         # find the node to delete
...         temp = self.root
        parent = None
        while temp is not None and temp.data != data:
            parent = temp
            if data < temp.data:
                temp = temp.left
            else:
                temp = temp.right
        if temp is None:
            return False

        # case 1: the node to delete has no children
        if temp.left is None and temp.right is None:
            if parent is None:
                self.root = None
            elif parent.left == temp:
                parent.left = None
            else:
                parent.right = None
        # case 2: the node to delete has one child
        elif temp.right is None:
            if parent is None:
                self.root = temp.left
            elif parent.left == temp:
                parent.left = temp.left
            else:
                parent.right = temp.left
        elif temp.left is None:
            if parent is None:
                self.root = temp.right
            elif parent.left == temp:
                parent.left = temp.right
            else:
                parent.right = temp.right
        # case 3: the node to delete has two children
        else:
            inheritor = temp.right
            while inheritor.left is not None:
                inheritor = inheritor.left
            temp.data = inheritor.data
            # delete the inheritor node
            self.delete(inheritor.data)

        return True
    
    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(node.data, end=' ')
            self.inorder(node.right)

    def postorder(self, node):
        if node is not None:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=' ')

    def preorder(self, node):
        if node is not None:
            print(node.data, end=' ')
            self.preorder(node.left)
            self.preorder(node.right)

# menu-driven interface
def main():
    tree = BinaryTree()
    while True:
        print("1. Insert a value")
        print("2. Search for a value")
        print("3. Delete a value")
        print("4. Inorder traversal")
        print("5. Postorder traversal")
        print("6. Preorder traversal")
        print("7. Quit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            value = int(input("Enter the value to insert: "))
            tree.insert(value)
        elif choice ==2:
            value = int(input("Enter the value to search: "))
            if tree.search(value)==False:
                print("Element not present")
            else: 
                print("Element present")
            
        elif choice ==3:
            value = int(input("Enter the value which you want to delete: "))
            tree.delete(value)
        elif choice == 4:
            tree.inorder(tree.root)
            print()
        elif choice == 5:
            tree.postorder(tree.root)
            print()
        elif choice == 6:
            tree.preorder(tree.root)
            print()
        elif choice==7:
            break;
if __name__ == '__main__':
