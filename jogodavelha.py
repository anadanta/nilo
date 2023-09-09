def print_board(board):
    print("   |   |")
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print("   |   |")

def check_winner(board, player):
    return ((board[0] == player and board[1] == player and board[2] == player) or
            (board[3] == player and board[4] == player and board[5] == player) or
            (board[6] == player and board[7] == player and board[8] == player) or
            (board[0] == player and board[3] == player and board[6] == player) or
            (board[1] == player and board[4] == player and board[7] == player) or
            (board[2] == player and board[5] == player and board[8] == player) or
            (board[0] == player and board[4] == player and board[8] == player) or
            (board[2] == player and board[4] == player and board[6] == player))

def tic_tac_toe():
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    current_player = "X"
    winner = None
    print("Bem-vindo ao Jogo da Velha!")
    print_board(board)
    
    while not winner and " " in board:
        move = int(input("Digite a posição para jogar (1-9): ")) - 1
        if board[move] == " ":
            board[move] = current_player
            print_board(board)
            if check_winner(board, current_player):
                winner = current_player
            else:
                current_player = "O" if current_player == "X" else "X"
        else:
            print("Posição inválida. Tente novamente.")
    
    if winner:
        print(f"Parabéns! O jogador {winner} venceu o jogo!")
    else:
        print("Empate!")
        
tic_tac_toe()
