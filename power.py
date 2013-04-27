def power(x, n):
  if n==1 or n==0:
    return x
  if n%2==0:
    return power(x, n/2) * power(x, n/2)
  else:
    return power(x, (n-1)/2) * power(x, (n-1)/2) * x

print power(4, 5)
print power(4, 6)
