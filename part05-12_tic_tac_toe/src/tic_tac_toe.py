def play_turn(game_board: list, x: int, y: int, piece: str) -> bool:
   
    if x < 0 or x >= 3 or y < 0 or y >= 3:
        return False
    
  
    if game_board[y][x] == "":
       
        game_board[y][x] = piece
        return True
    else:
       
        return False

if __name__ == "__main__":
    game_board = [["", "", ""], ["", "", ""], ["", "", ""]]
    print(play_turn(game_board, 2, 0, "o"))  
    print(game_board)  