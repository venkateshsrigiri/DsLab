Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def quick_sort(array):
...     if len(array) < 2:
...         return array
...     pivot = array[0]
...     less = [i for i in array[1:] if i <= pivot]
...     greater = [i for i in array[1:] if i > pivot]
...     return quick_sort(less) + [pivot] + quick_sort(greater)
... data= []
... qs=int(input("Enter Size"))
... for i in range (qs):
...         a=input()
...         data.append(a)
... last = quick_sort(data)
