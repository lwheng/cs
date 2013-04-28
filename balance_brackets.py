def balance_brackets(string):
  left_count = 0
  is_open = False
  temp = ''
  last_good = ''
  for a in string:
    if a == '(':
      left_count += 1
      is_open = True
      temp += a
    elif a == ')':
      left_count -= 1
      temp += a
      if left_count == 0:
        is_open = False
    else:
      temp += a

    if left_count == 0 and is_open == False:
      last_good = temp
  return last_good


print balance_brackets("(ab(xy)u)2)")
print balance_brackets(")))(((")
print balance_brackets("()ab(aa)(")
