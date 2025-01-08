# Write your solution here
def who_won(game_board: list):
    player1_count = 0
    player2_count = 0

    for row in game_board:
        for cell in row:
            if cell == 1:
                player1_count += 1
            elif cell == 2:
                player2_count += 1

    if player1_count > player2_count:
        return 1
    elif player2_count > player1_count:
        return 2
    else:
        return 0

# Testowanie funkcji
if __name__ == "__main__":
    game_board = [
        [0, 1, 1, 2],
        [1, 1, 2, 2],
        [0, 2, 1, 0],
        [2, 1, 1, 2]
    ]
    print(who_won(game_board))  # Powinno wydrukować 0, ponieważ obaj gracze mają po 6 kamieni