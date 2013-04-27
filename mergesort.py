def mergesort(A):
  if (len(A) <= 1):
     return A
  middle = len(A) / 2
  left = []
  right = []
  for i in range(0, middle):
    left.append(A[i])
  for i in range(middle, len(A)):
    right.append(A[i])
  left = mergesort(left)
  right = mergesort(right)
  return merge(left, right)

def merge(left, right):
  result = []
  while (len(left) > 0 or len(right) > 0):
    if (len(left) > 0 and len(right) > 0):
      if (left[0] <= right[0]):
        result.append(left[0])
        left = left[1:]
      else:
        result.append(right[0])
        right = right[1:]
    elif (len(left) > 0):
      result.append(left[0])
      left = left[1:]
    elif (len(right) > 0):
      result.append(right[0])
      right = right[1:]
  return result

import random
from datetime import datetime
A = range(1,1000)
random.shuffle(A)
print datetime.now()
mergesort(A)
print datetime.now()
