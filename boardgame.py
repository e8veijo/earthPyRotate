# Board game
# input grid needs to be square 2x2, 3x3, 4x4 ...
# brick ID's needs to be integers of max size 999
# brick ids needs to have whitespace boundaries
# please be free to make your own brick

import os, sys, time

in_file     = "board.txt"
game_on     = True
bricks      = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P']


def get_board():
    lines = []
    with open(in_file, 'r') as fp:
        lines = fp.readlines()
    return lines
    
def print_board(board):
    for i in range(0, len(board)):
        print(board[i])
        
def print_help():
    print("+----------------------+")
    print("!      RULES           !")
    print("+----------------------+")
    print("! Task is to sort out  !")
    print("! NUM    = move        !")
    print("! ZERO   = quit        !")
    print("! h      = help        !")
    print("+----------------------+")
    
def create_x_y_z_bricks(board):
    bricks      = []
    i_brick     = 0
    
    for i in range(0, len(board)):
        row = board[i]
        
        for c in row:
            print(c, end='')
        print('')

    return bricks
    
def move_board(ik, board):
    print("moved {ik} on board")

def main():
    board = get_board()
    
    if not board:
        print("Board file is empty")
        sys.exit()
        
    os.system('clear')

    # Strip all newline-symbols
    for i in range(0, len(board)):
        board[i] = board[i].strip('\n')
        
    print("DEBUG Board width: " + str( len( board[0] ) ) )
    print("DEBUG Board higth: " + str( len( board ) ) )
    
    # just print the lines
    print_board( board )
    print("This is the key map")
    print_help()
    
    bricks = create_x_y_z_bricks(board)
        
    input("Press Enter to start IQ game...")
    
    while game_on:
        os.system('clear')
        print_board(board)
        ik = input("Move: ")
        print("You pressed: "+ ik)
        
        if ik == 'h':
            print_help()
        elif ik == '0':
            print("Why you quit so soon dear cute sir miss!")
            time.sleep(2.0)
            sys.exit()
        elif ik == '1':
            move_board(ik, board)
        time.sleep(1.0)
        #sys.exit()
        
if __name__ == "__main__":
    main()