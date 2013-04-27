def maxsubsetsum(A):
  tempsum = 0
  maxsum = 0
  tempsumstartindex = 0
  maxsumstart = 0
  maxsumend = 0
  for i in range(0, len(A)):
    futuresum = tempsum + A[i]
    if futuresum > 0:
      tempsum = futuresum
      if tempsum > maxsum:
        maxsum = tempsum
        maxsumstart = tempsumstartindex
        maxsumend = i
    else:
      tempsum = 0
      tempsumstartindex = i+1
  print "Max Start Index " + str(maxsumstart)
  print "Max End Index " + str(maxsumend)
  return maxsum

A = [-1,-1,3,-2]
print maxsubsetsum(A)
