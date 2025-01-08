# Write your solution here
def print_sudoku(sudoku):
    row_index = 0
    while row_index < len(sudoku):  # Pętla iterująca przez wiersze planszy Sudoku
        row = sudoku[row_index]     # Pobieranie bieżącego wiersza
        col_index = 0               # Indeks kolumny
        while col_index < len(row):  # Pętla iterująca przez kolumny w bieżącym wierszu
            if col_index > 0 and col_index % 3 == 0:  # Dodawanie odstępu co 3 kolumny
                print(' ', end=' ')
            if row[col_index] == 0:  # Jeśli wartość w komórce jest 0
                print('-', end=' ')  # Drukowanie '-' zamiast 0
            else:  # Jeśli wartość w komórce nie jest 0
                print(row[col_index], end=' ')  # Drukowanie wartości z komórki
            col_index += 1
        print()  # Dodajemy nową linię po każdym wierszu
        if (row_index + 1) % 3 == 0 and row_index + 1 < len(sudoku):
            print()  # Dodajemy dodatkową linię po każdym trzecim wierszu
        row_index += 1

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    # Tworzymy kopię planszy Sudoku
    sudoku_copy = [row[:] for row in sudoku]
    # Dodajemy liczbę do kopii planszy
    sudoku_copy[row_no][column_no] = number
    return sudoku_copy

# Testowanie funkcji
if __name__ == "__main__":
    sudoku = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)