def heapify(A, idx, max):
  left = 2*idx + 1
  right = 2*idx + 2

  if (left < max and A[left] > A[idx]):
    largest = left
  else:
    largest = idx
  if (right < max and A[right] > A[largest]):
    largest = right
  if (largest != idx):
     temp = A[idx]
     A[idx] = A[largest]
     A[largest] = temp
     heapify(A, largest, max)

def buildheap(A):
  for i in xrange(len(A)/2 - 1, -1, -1):
    heapify(A,i,len(A))

def heapsort(A):
  buildheap(A)
  for i in xrange(len(A)-1, 0, -1):
    temp = A[0]
    A[0] = A[i]
    A[i] = temp
    heapify(A, 0, i)

import random
from datetime import datetime
A = range(1,1000)
random.shuffle(A)
print datetime.now()
heapsort(A)
print datetime.now()
