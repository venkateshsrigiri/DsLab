Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def insertion_sort(V):
... 	for i in range(1, len(V)):
... 		k =V[i]
... 		j = i-1
... 		while j >=0 and k < V[j] :
... 				V[j+1] = V[j]
... 				j -= 1
... 		V[j+1] = k
... V = [12, 11, 13, 5, 6]
... insertion_sort(V)
... l2 = []
... print("Sorted array is : ")	 
