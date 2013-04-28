def simple_regex_parser(regex):
  star = '*'
  plus = '+'
  dot = '.'

  regex_list = ['*', '+', '.']

  temp = ''

  for i in range(0, len(regex)):
    if regex[i] in regex_list:
      print regex[i] + " " + temp
      temp = ''
    else:
      temp = regex[i]


simple_regex_parser("hello*wor+ld.")
