class TicTAcToe:
    def __init__(self):
        self.board = ["1","2","3","4","5","6","7","8","9"]
        self.turn = 1

    def wining(self):
        if self.turn % 2 == 0:
            print("X Won!")
        else:
            print("O Won!")
        exit()

    def show_board(self):
        print("\n" + self.board[0] + " | " + self.board[1] + " | " + self.board[2])
        print("--+---+--")
        print(self.board[3] + " | " + self.board[4] + " | " + self.board[5])
        print("--+---+--")
        print(self.board[6] + " | " + self.board[7] + " | " + self.board[8])

        if self.board[0] == self.board[1] and self.board[1] == self.board[2]:
            self.wining()
        elif self.board[3] == self.board[4] and self.board[4] == self.board[5]:
            self.wining()
        elif self.board[6] == self.board[7] and self.board[7] == self.board[8]:
            self.wining()
        elif self.board[0] == self.board[3] and self.board[3] == self.board[6]:
            self.wining()
        elif self.board[1] == self.board[4] and self.board[4] == self.board[7]:
            self.wining()
        elif self.board[2] == self.board[5] and self.board[5] == self.board[8]:
            self.wining()
        elif self.board[0] == self.board[4] and self.board[4] == self.board[8]:
            self.wining()
        elif self.board[2] == self.board[4] and self.board[4] == self.board[6]:
            self.wining()  
        open.play()

    def play(self):
        if self.turn == 10:
            print("Draw!")
            exit()
        while True:
            try:
                if self.turn % 2 == 0:
                    print("O Turn")
                else:
                    print("X Turn")
                turn = int(input("Enter Choice (1-9): "))
                if turn > 0 and turn < 10 and self.board[turn - 1] != "X" and self.board[turn - 1] != "O":
                    break
                print("Enter Valid Value!")
            except ValueError:
                print("Enter Only Numbers!")
        self.turn += 1
        new_turn = turn - 1
        if self.turn % 2 == 0:
            self.board[new_turn] = "X"
        else:
            self.board[new_turn] = "O"

        open.show_board()
open = TicTAcToe()
open.show_board()

