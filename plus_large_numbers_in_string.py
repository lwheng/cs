def plus_2_digits(d1,d2):
  return int(d1) + int(d2)

def plus_2_large_numbers_in_string(d1, d2):
  result = ''
  if (len(d1) >= len(d2)):
    top = d1
    bot = d2
  else:
    top = d2
    bot = d1

  index_top = len(top) - 1
  index_bot = len(bot) - 1
  carry = False

  while index_bot >= 0:
    temp = plus_2_digits(top[index_top], bot[index_bot])
    if carry == True:
      temp += 1
      carry = False
    if temp >= 10:
      carry = True
    result = str(temp)[-1] + result
    index_bot -= 1
    index_top -= 1
  while index_top >= 0:
    temp = plus_2_digits(top[index_top], 0)
    if carry == True:
      temp += 1
      carry = False
    if temp >= 10:
      carry = True
    result = str(temp)[-1] + result
    index_top -= 1
  return result

print plus_2_large_numbers_in_string("1982730192381702398172301982371", "4783190471982371029831720312")

