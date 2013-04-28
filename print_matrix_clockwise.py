def print_row_right(A, col_start, col_end, row, cells):
  for i in range(col_start, col_end+1):
    print A[row][i]
    cells-=1
  return cells

def print_row_left(A, col_start, col_end,row, cells):
  for i in xrange(col_start, col_end-1, -1):
    print A[row][i]
    cells-=1
  return cells

def print_col_down(A, row_start, row_end, col, cells):
  for i in range(row_start, row_end+1):
    print A[i][col]
    cells-=1
  return cells

def print_col_up(A, row_start, row_end, col, cells):
  for i in xrange(row_start, row_end-1, -1):
    print A[i][col]
    cells-=1
  return cells

def print_matrix_clockwise(A, row_start, row_end, col_start, col_end, cells):
  cells = print_row_right(A, col_start, col_end, row_start, cells)
  cells = print_col_down(A, row_start+1, row_end, col_end, cells)
  cells = print_row_left(A, col_end-1, col_start, row_end, cells)
  cells = print_col_up(A, row_end-1, row_start+1, col_start, cells)
  return cells

A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
cells = 16
row_start = 0
row_end = 3
col_start = 0
col_end = 3
while cells > 0:
  cells = print_matrix_clockwise(A, row_start, row_end, col_start, col_end, cells)
  row_start+=1
  row_end-=1
  col_start+=1
  col_end-=1
