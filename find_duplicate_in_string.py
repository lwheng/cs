def find_duplicate_in_string(A):
  this_dict = {}
  middle = len(A) / 2
  left = 0
  right = len(A) - 1
  while left!=middle or right!=middle:
    leftchar = A[left]
    rightchar = A[right]
    if leftchar not in this_dict:
      this_dict[leftchar] = 0
    this_dict[leftchar] += 1
    if rightchar not in this_dict:
      this_dict[rightchar] = 0
    this_dict[rightchar] += 1
    left += 1
    right -= 1
  print this_dict

A = "hello world"
find_duplicate_in_string(A)
