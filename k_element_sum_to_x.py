def k_element_sum_to_x(A, k, x):
  A = mergesort(A)
  subset = [0] * k
  findAllCombi(A, subset, 0, 0, x)

def findAllCombi(A, subset, setIndex, subSetIndex, x):
  if (len(subset) == subSetIndex):
    check_sum(subset, x)
  else:
    for i in range(setIndex, len(A)):
      subset[subSetIndex] = A[i]
      findAllCombi(A, subset, i+1, subSetIndex+1, x)

def check_sum(A, x):
  total = 0
  for a in A:
    total += a
  if total == x:
    print A
  
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

A = [1,2,3,4,5,6,7,8,9,-4,-3,-1]
k = 2
x = 5
print "k = " + str(k)
print "x = " + str(x)
k_element_sum_to_x(A,k,x)
