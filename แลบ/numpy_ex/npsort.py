import numpy as np

a = [2, 3, 9, 1, 4]

a.sort(reverse=False)
# return a as sort list ascending
print(a)

a = [2, 3, 9, 1, 4]
# return index of sorting array
indx = np.argsort(a)
print(indx)
print(a)

# convert list a to np array
print(np.array(a)[indx])
