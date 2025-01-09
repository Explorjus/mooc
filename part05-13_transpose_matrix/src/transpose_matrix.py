# Write your solution here
def transpose(matrix: list) -> list:
    # Tworzymy nową macierz o wymiarach odwrotnych do oryginalnej
    transposed = [[0] * len(matrix) for _ in range(len(matrix[0]))]
    
    # Zamieniamy wiersze z kolumnami
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            transposed[j][i] = matrix[i][j]
    
    print(transposed)

# Testowanie funkcji
if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    transposed_matrix = transpose(matrix)
    print(transposed_matrix)