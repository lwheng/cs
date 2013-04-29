def simple_find(A):
  item = A[0]
  index = -1
  for i in range(1, len(A)):
    if item < A[i]:
      item = A[i]
    else:
      return i
  return index

def simple_find2(A):
  return len(A) - (A[0] - 1)
  

def rotate_array(A, shift):
  return A[shift:] + A[0:shift]

A = range(1,10)
A = rotate_array(A, 3)
print A
print simple_find(A)
print simple_find2(A)
