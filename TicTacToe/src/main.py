# This is a game of tic-tac-toe.
# by Zakery Sattler


def create_board():
    board = []
    for square in range(9):
        board.append(square + 1)
    return board


def display_board(board):
    print('')
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print('-----------')
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print('-----------')
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print('')


def is_winner(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6]
            )


def is_draw(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


def make_move(player, board):
    square = int(input(f"{player}'s turn to choose a square (1-9): "))
    board[square - 1] = player


def next_player(player):
    return 'O' if player == 'X' else 'X'


def main():
    print('')
    print('This is a game of Tic-Tac-Toe. X goes first!')
    player = next_player("")
    board = create_board()
    
    while not():
        display_board(board)
        make_move(player, board)
        player = next_player(player)
        

        if is_winner(board):
            display_board(board)
            print("")
            print("Hooray you won the game!")
            print("Thanks for playing!")
            print("")

        
        if is_draw(board):
            display_board(board)
            print('')
            print("It is a Tie")
            print('')

       
    
    

if __name__ == "__main__":
    main()

