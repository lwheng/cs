def p_in_big_string(big, p, A):
  len_p = len(p)
  len_big = len(big)
  len_A = len(A)
  len_each = len(A[0])

  for i in xrange(0, len_big, len_each):
    if p == big[i:i+len_p]:
      return i

A = ['she', 'all', 'get', 'sun', 'for', 'fun']
import random
from random import choice
index = range(0,len(A))
index1 = range(1, 20)
random.shuffle(index)
big = ''
p = ''
for i in index:
  p += A[i]
front = choice(index1)
back = choice(index1)
for i in range(0, front):
  big += choice(A)
big += p
for i in range(0, back):
  big += choice(A)

print big
print p
print
answer = p_in_big_string(big, p, A)
print answer
print big[answer:answer+len(p)]
