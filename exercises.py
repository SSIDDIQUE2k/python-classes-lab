# step one
class Game ():
    def __init__(self):
        self.turn = 'X'
        self.tie = False
        self.winner = None
        self.board = {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None,
        }
        # step 2
    def play_game(self):
        print("Welcome to Tic Tac Toe!")
        print("Here is the current board:")
        print(self.board)
        while True:
            break
game_instance = Game()
game_instance.play_game()

def print_board(self):
  b = self.board
  print(f"""
        A   B   C
    1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
        ----------
    2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
        ----------
    3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
  """)
# step 3
def print_message(self):
    ## If there is a tie: print("Tie game!")
    if self.tie:
        print("Tie game!")
    ## If there is a winner: print(f"{self.winner} wins the game!")
    elif self.winner:
        print(f"{self.winner} wins the game!")

    ## Otherwise: print(f"It's player {self.turn}'s turn!")
    else:
        print(f"It's player {self.turn}'s turn!")

def render(self):
    # Call upon print_board
    self.print_board()
    ## Call upon print_message
    self.print_message()


# step 4
    while True:
    # prompt user for input
        move = input("Enter a valid move (example: A1): ").strip().lower()
        # If the input is valid, update the board and break the loop
        if move in self.board and not self.board[move]:
            self.board[move] = self.turn
            break
    # otherwise, print a message notifying the user of the invalid input and allow the loop to continue
    else:
        print("Invalid move. Please try again.")

#step 5
# Next, create a method for determining a winner by checking the board for the eight possible winning combinations. Upon detecting a winning combination, update the winner attribute to reflect the current player (turn).

# A loop of some sort would be appropriate, but you can also check each combination manually:
winning_combinations = [
    ('a1', 'b1', 'c1'),
    ('a2', 'b2', 'c2'),
    ('a3', 'b3', 'c3'),
    ('a1', 'a2', 'a3'),
    ('b1', 'b2', 'b3'),
    ('c1', 'c2', 'c3'),
    ('a1', 'b2', 'c3'),
    ('c1', 'b2', 'a3')
]
















    






