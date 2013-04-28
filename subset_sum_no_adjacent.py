def subset_sum_no_adjacent(A):
  sum_list = [0] * (len(A) + 1)
  sum_list[0] = 0
  sum_list[1] = max(sum_list[0], A[1-1])
  for i in range(2, len(sum_list)):
    sum_list[i] = max(sum_list[i-2] + A[i-1], sum_list[i-1])
  return sum_list[-1]

A = [23,44,112,42,50]
print A
print subset_sum_no_adjacent(A)

