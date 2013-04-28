def division_without_division(num, divisor):
  count = 0
  temp = num
  while temp >= 0 and temp > divisor:
    temp -= divisor
    count += 1
  return (temp, count)

print division_without_division(100,3)
