Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_front(self, data):
        # Insert a new node at the beginning of the list
        new_node = Node(data, self.head)
        self.head = new_node

    def insert_at_end(self, data):
        # Insert a new node at the end of the list
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def delete_node(self, data):
        # Delete the first node with the given data
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        temp = self.head
        while temp.next:
            if temp.next.data == data:
                temp.next = temp.next.next
                return
            temp = temp.next

    def find_node(self, data):
        # Find the first node with the given data and return it, or return None if not found
        temp = self.head
        while temp:
            if temp.data == data:
                return temp
            temp = temp.next
        return None

    def print_list(self):
        # Print the data in each node of the list
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

... 
... def print_menu():
...     print('1. Insert at front')
...     print('2. Insert at end')
...     print('3. Delete node')
...     print('4. Find node')
...     print('5. Print list')
...     print('6. Quit')
...     print()
... 
... 
... LL = LinkedList()
... 
... while True:
...     print_menu()
...     choice = int(input('Enter your choice: '))
... 
...     if choice == 1:
...         data = input('Enter data to insert: ')
...         LL.insert_at_front(data)
...     elif choice == 2:
...         data = input('Enter data to insert: ')
...         LL.insert_at_end(data)
...     elif choice == 3:
...         data = input('Enter data to delete: ')
...         LL.delete_node(data)
...     elif choice == 4:
...         data = input('Enter data to find: ')
...         node = LL.find_node(data)
...         if node:
...             print('Node found:', node.data)
...         else:
...             print('Node not found')
...     elif choice == 5:
...         LL.print_list()
...     elif choice == 6:
...         break
...     else:
...         print('Invalid choice. Enter a number between 1 and 6.')
