# Given an array, remove all x's and then the resulted array is condensed

def list_eraser(A, x):
  while x in A:
    A.remove(x)
  return A

A = [1,3,0,3,1,0,6,5,0,87]
B = list_eraser(A,0)
print B
