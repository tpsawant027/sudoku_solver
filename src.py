import copy


def get_row(sudoku, k):
    return sudoku[k]

  
def get_col(sudoku, k):
    col = [sudoku[i][k] for i in range(len(sudoku))]
    return col

  
def get_box(sudoku, k):
    box = []
    if k in (0, 3, 6):
        for i in range(k, k+3):
            box.extend(sudoku[i][:3])
    elif k in (1, 4, 7):
        for i in range(k-1, k+2):
             box.extend(sudoku[i][3:6])   
    else:
        for i in range(k-2, k+1):
            box.extend(sudoku[i][6:9])
    return box

  
def first_empty_position(sudoku):
    for a, row in enumerate(sudoku):
        if not all(row):
            return (a, row.index(0))
    else:
        return (None, None)

      
def is_section_valid(nums):
    for n in set(nums):
        if nums.count(n) > 1 and n != 0:
            return False
    else:
        return True

      
def is_sudoku_valid(sudoku):
    rows_valid = all([is_section_valid(get_row(sudoku, i)) for i in range(0, 9)])
    cols_valid = all([is_section_valid(get_col(sudoku, i)) for i in range(0, 9)])
    boxes_valid = all([is_section_valid(get_box(sudoku, i)) for i in range(0, 9)])
    return rows_valid and cols_valid and boxes_valid

  
def is_section_complete(nums):
    if 0 in nums:
        return False
    elif len(set(nums)) == 9:
        return True
    else:
        return False

      
def is_sudoku_complete(sudoku):
    rows_complete = all([is_section_complete(get_row(sudoku, i)) for i in range(0, 9)])
    cols_complete = all([is_section_complete(get_col(sudoku, i)) for i in range(0, 9)])
    boxes_complete = all([is_section_complete(get_box(sudoku, i)) for i in range(0, 9)])
    return rows_complete and cols_complete and boxes_complete
  
  
def repeat(sudoku):
  if is_sudoku_complete(sudoku):
      return True
  i, j = first_empty_position(sudoku)
  for a in range(1, 10):
      sudoku[i][j] = a
      if is_sudoku_valid(sudoku):
         if repeat(sudoku):
          return True
      sudoku[i][j] = 0
  return False


def sudoku_solver(sudoku):
  copied_sudoku = copy.deepcopy(sudoku)
  if repeat(copied_sudoku):
      return copied_sudoku
  return None
