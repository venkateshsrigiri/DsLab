Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def linear_search(data, pivot):
...     for i in range(len(data)):
...         if data[i] == pivot:
...             print("Data found at:",i)
...     
... 
... def main():
...     data = []
...     V=int(input("Enter size of list"))
...     for i in range (V):
...         a=input()
...         data.append(a)
...     pivot = input("Enter a pivot value: ")
...     index = linear_search(data, pivot)
...         
... 
... if __name__ == '__main__':
