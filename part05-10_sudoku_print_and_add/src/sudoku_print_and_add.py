# Write your solution here
def print_sudoku(sudoku):
    row_index = 0
    while row_index < len(sudoku):  #pętla gdy row_index jest mniejsze od dlugoćci listy sudoku
        row = sudoku[row_index]     #doda nie zmiennej row w petli while która jest ineksem z listy sudoku
        col_index = 0               #indeks kolumny
        while col_index < len(row):          #pętla kiedy ineks kolumny jest mneijszy od dlugosci zmiennej row
            if col_index > 0 and col_index % 3 == 0:     #jesli indeks kolumny jest > 0 i dzielnie przez 3 daje reszte 0
                print(' ', end=' ')                      #print odstepu co 3 kolumny
            if row[col_index] == 0:                      #jesli indeks rzedu w odniesiueniu do ineksu columny = 0 
                print('_', end=' ')                      #zamiana 0 na -
            else:
                print(row[col_index], end=' ') 
                     
            col_index += 1
        print()  # Dodajemy nową linię po każdym wierszu
        if (row_index + 1) % 3 == 0 and row_index + 1 < len(sudoku):
            print()  # Dodajemy dodatkową linię po każdym trzecim wierszu
        row_index += 1

def add_number(sudoku, row_no, column_no, number):
    sudoku[row_no][column_no] = number

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

    print_sudoku(sudoku)
    
    add_number(sudoku, 0, 0, 2)
    add_number(sudoku, 1, 2, 7)
    add_number(sudoku, 5, 7, 3)
    print()
    print_sudoku(sudoku)