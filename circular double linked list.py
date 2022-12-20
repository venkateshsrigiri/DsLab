Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class Node:
    def __init__(self, data=None, prev=None, next=None):
...         self.data = data
...         self.prev = prev
...         self.next = next
... 
... class CircularDoubleLinkedList:
...     def __init__(self):
...         self.head = None
... 
...     def append(self, data):
...         new_node = Node(data, None, None)
...         if self.head is None:
...             self.head = new_node
...             new_node.prev = self.head
...             new_node.next = self.head
...         else:
...             temp_node = self.head
...             while temp_node.next != self.head:
...                 temp_node = temp_node.next
...             temp_node.next = new_node
...             new_node.prev = temp_node
...             new_node.next = self.head
...             self.head.prev = new_node
... 
...     def prepend(self, data):
...         new_node = Node(data, None, None)
...         if self.head is None:
...             self.head = new_node
...             new_node.prev = self.head
...             new_node.next = self.head
...         else:
...             temp_node = self.head
...             while temp_node.next != self.head:
...                 temp_node = temp_node.next
...             temp_node.next = new_node
...             new_node.prev = temp_node
...             new_node.next = self.head
...             self.head.prev = new_node
...             self.head = new_node
... 
...     def delete(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            temp_node = self.head
            while temp_node.next != self.head:
                temp_node = temp_node.next
            if self.head == self.head.next:
                self.head = None
            else:
                temp_node.next = self.head.next
                self.head.next.prev = temp_node
                self.head = self.head.next
        else:
            temp_node = self.head
            while temp_node.next != self.head:
                if temp_node.next.data == data:
                    temp_node.next = temp_node.next.next
                    temp_node.next.prev = temp_node
                    break
                temp_node = temp_node.next

    def display(self):
        elements = []
        temp_node = self.head
        while temp_node:
            elements.append(temp_node.data)
            temp_node = temp_node.next
            if temp_node == self.head:
                break
        print(elements)

cdl = CircularDoubleLinkedList()

while True:
    print("Menu:")
    print("1. Append an element")
    print("2. Prepend an element")
    print("3. Delete an element")
    print("4. Display the list")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = input("Enter the element to append: ")
        cdl.append(data)
    elif choice == 2:
        data = input("Enter the element to prepend: ")
        cdl.prepend(data)
    elif choice == 3:
        data = input("Enter the element to delete: ")
        cdl.delete(data)
    elif choice == 4:
        cdl.display()
    elif choice == 5:
