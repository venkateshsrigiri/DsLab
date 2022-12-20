Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def binary_search(data, pivot):
...     low = 0
...     high = len(data) - 1
...     while low <= high:
...         mid = (low + high) // 2
...         if data[mid] == pivot:
...             return mid
...         elif data[mid] < pivot:
...             low = mid + 1
...         else:
...             high = mid - 1
...     return -1
... 
... def main():
...     data = []
...     limit=int(input("Enter size of list"))
...     for i in range (limit):
...         a=input()
...         data.append(a)
...     pivot = input("Enter a pivot value: ")
...     index = binary_search(data, pivot)
...     if index == -1:
...         print("Value not found")
...     else:
...         print("Value found at index", index)
... 
... if __name__ == '__main__':
