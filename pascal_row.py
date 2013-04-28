import math
def pascal_row(row):
  if row == 0:
    print 1
  else:
    for i in range(0, row+1):
      print n_choose_k(row, i)

def n_choose_k(n, k):
  return math.factorial(n) / ((math.factorial(k))*(math.factorial(n-k)))

pascal_row(3)
