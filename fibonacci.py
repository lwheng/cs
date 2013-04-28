def recursive(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return recursive(n-1) + recursive(n-2)

def iterative(n):
  (a,b) = (0,1)
  for i in range(n):
    (a,b) = (b, a+b)
  return a

n=25
from datetime import datetime
print datetime.now()
print recursive(n)
print datetime.now()
print iterative(n)
print datetime.now()

