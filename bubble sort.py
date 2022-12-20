Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> V=[5,3,7,8,2,1]
... n=len(V)
... print("Original:",V)
... for i in range(n-1):
...     for j in range(n-1):
...         if V[j]>V[j+1]:
...             V[j],V[j+1]=V[j+1],V[j]
