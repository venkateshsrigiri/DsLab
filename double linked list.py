Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Node:
...     def __init__(self, data=None, prev=None, next=None):
...         self.data = data
...         self.prev = prev
...         self.next = next
... 
... class DoubleLinkedList:
...     def __init__(self):
...         self.head = None
...         self.tail = None
... 
...     def append(self, data):
...         new_node = Node(data, None, None)
...         if self.head is None:
...             self.head = new_node
...             self.tail = new_node
...         else:
...             new_node.prev = self.tail
...             new_node.next = None
...             self.tail.next = new_node
...             self.tail = new_node
... 
...     def prepend(self, data):
...         new_node = Node(data, None, None)
...         if self.head is None:
...             self.head = new_node
...             self.tail = new_node
...         else:
...             new_node.next = self.head
...             self.head.prev = new_node
...             self.head = new_node
... 
...     def delete(self, data):
...         temp_node = self.head
...         while temp_node is not None:
...             if temp_node.data == data:
...                 if temp_node.prev is not None:
                    temp_node.prev.next = temp_node.next
                    temp_node.next.prev = temp_node.prev
                else:
                    self.head = temp_node.next
                    temp_node.next.prev = None
                break
            temp_node = temp_node.next

    def display(self):
        elements = []
        temp_node = self.head
        while temp_node is not None:
            elements.append(temp_node.data)
            temp_node = temp_node.next
        print(elements)

dll = DoubleLinkedList()

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
        dll.append(data)
    elif choice == 2:
        data = input("Enter the element to prepend: ")
        dll.prepend(data)
    elif choice == 3:
        data = input("Enter the element to delete: ")
        dll.delete(data)
    elif choice == 4:
        dll.display()
    elif choice == 5:
        break
    else:
