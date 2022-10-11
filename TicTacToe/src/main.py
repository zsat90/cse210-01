# This is a game of tic-tac-toe.
# by Zakery Sattler



def create_board():
    board = []
    for square in range(9):
        board.append('-')
    return board


def display_board(board):
    print('')
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print('------------')
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print('-----------')
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print('')


def is_winner(board, let):
    return((board[0] == let and board[1] == let and board[2] == let) or
        (board[3] == let and board[4] == let and board[5] == let) or
        (board[6] == let and board[7] == let and board[8] == let) or
        (board[1] == let and board[4] == let and board[7] == let) or
        (board[2] == let and board[5] ==  let and board[8] == let) or
        (board[0] == let and board[4] == let and board[8] == let) or
        (board[2] == let and board[4] ==  let and board[6] == let) or
        (board[0] == let and board[3] == let and board[6] == let)
        )
        


def is_draw(board):
    for row in board:
        for i in row:
            if i == '-':
                return False
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
    is_playing = True
    
    while (is_playing == True):
        display_board(board)
        make_move(player, board)
        player = next_player(player)
    
        

        if is_winner(board, 'O'):
            display_board(board)
            is_playing = False
            print("")
            print("Hooray O you won the game!")
            print("Thanks for playing!")
            print("")
            
        elif is_winner(board, 'X'):
            display_board(board)
            is_playing = False
            print("")
            print("Hooray X you won the game!")
            print("Thanks for playing!")
            print("")
        
        elif is_draw(board):
            is_playing = False
            display_board(board)
            print('')
            print("It is a Tie")
            print('')
            

       
    
    

if __name__ == "__main__":
    main()

