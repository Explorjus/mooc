# Write your solution here
# Write your solution here
def column_correct(sudoku, column_no):
    seen = []
    for row in sudoku:
        num = row[column_no]
        if num != 0:
            if num in seen:
                return False
            seen.append(num)
    return True
                 
 
  
    

if __name__ == "__main__":
# Testowanie funkcji
    sudoku = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
     ]

    print(column_correct(sudoku, 0))  # Powinno wydrukować True
    print(column_correct(sudoku, 1))  # Powinno wydrukować False