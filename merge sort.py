Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def merge(list):
...     if len(list)>1:
...         mid=len(list)//2
...         left=list[:mid]
...         right=list[mid:]
...         merge(left)
...         merge(right)
...         i=0
...         j=0
...         k=0
...         while i<len(left) and j<len(right):
...             if left[i]<=right[j]:
...                 list[k]=left[i]
...                 i=i+1
...             else:
...                 list[k]=right[j]
...                 j=j+1
...             k=k+1
...         while i<len(left):
...             list[k]=left[i]
...             i=i+1
...             k=k+1
...         while j<len(right):
...             list[k]=right[j]
...             j=j+1
...             k=k+1
... 
... list=[]
... limit=int(input("Enter size of list"))
...     for i in range (limit):
...         a=input()
...         list.append(a)
... print("before sorting:",list)
... merge(list)
