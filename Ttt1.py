player_turn = 1
board = ["1","2","3","4","5","6","7","8","9"]

def wining(a):
    if a % 2 == 0:
        print("X Won!")
    else:
        print("O Won!")
    exit()

def show_board(a):
    print("\n" + board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])

    if board[0] == board[1] and board[1] == board[2]:
        wining(a)
    elif board[3] == board[4] and board[4] == board[5]:
        wining(a)
    elif board[6] == board[7] and board[7] == board[8]:
        wining(a)
    elif board[0] == board[3] and board[3] == board[6]:
        wining(a)
    elif board[1] == board[4] and board[4] == board[7]:
        wining(a)
    elif board[2] == board[5] and board[5] == board[8]:
        wining(a)
    elif board[0] == board[4] and board[4] == board[8]:
        wining(a)
    elif board[2] == board[4] and board[4] == board[6]:
        wining(a)  
    play(a)

def play(a):
    if a == 10:
        print("Draw!")
        exit()
    while True:
        try:
            if a % 2 == 0:
                print("O Turn")
            else:
                print("X Turn")
            turn = int(input("Enter Choice (1-9): "))
            if turn > 0 and turn < 10 and board[turn - 1] != "X" and board[turn - 1] != "O":
                break
            print("Enter Valid Value!")
        except ValueError:
            print("Enter Only Numbers!")
    a += 1
    new_turn = turn - 1
    if a % 2 == 0:
        board[new_turn] = "X"
    else:
        board[new_turn] = "O"

    show_board(a)
show_board(player_turn)

