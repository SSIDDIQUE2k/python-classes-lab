# Step 1 - Define a Game class and initialize game state
# Create a class called Game. Within the Game class, use the __init__ method to initialize properties that represent the state of your game.

# Below are some of the attributes you might include:

# turn: a string attribute indicating whose turn it is ('X' or 'O'). Initialize it with 'X'.
# tie: a boolean attribute indicating if the game ended in a tie. Initialize it as False.
# winner: an attribute to store the game-winner. Initialize it as None.
# board: a dictionary representing the state of the game board:

class Game:
    def __init__(self):
        self.turn = 'X'
        self.tie = False
        self.winner = None
        self.board = {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None,
        }
#         Next, define a play_game method and confirm that the method is accessible on an instance of the Game class. This function will be used to activate and organize the flow of the game.

# Within the play_game method, print a welcome message of your choosing.
# Instantiate the Game class and invoke the play_game method:

        # step 2

    def play_game(self):
        print("Welcome To TIC_TAC_TOE, Shall We Play a Game?")
        self.render()
# Step 3 - Rendering
# Next, you’ll want to define methods that can ‘render’ information for the user. Based on the separation of concerns, you might break this logic down into two or three methods.

# Consider the following approach:

# Rendering the board
# The print_board method visualizes the current state of the game board.

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

#         Rendering messages
# The print_message method updates users about the current status of a game, including whose turn it is, who won the game, and if the game ended in a tie.
    
    def print_message(self):
        if self.tie:
            print("It's a Tie Game!")
        elif self.winner:
            print(f"{self.winner} wins the game!")
        else:
            print(f"It's player {self.turn}'s turn!")

# Step 4 - Handling player input
# Next, you’ll need a method to handle user input, such as get_move or place_piece. This method should prompt a user to enter the key of an empty space on the board.

# To capture player input, use the input() function. This function displays a prompt in the terminal and returns the string that the user enters.
    def get_move(self):
        while True:
            move = input(f"Enter a valid move (example: A1): ").lower()
            if move in self.board and self.board[move] is None:
                return move
            else:
                print("Invalid move, try again!")


#     Step 5 - Checking for a winner
# Next, create a method for determining a winner by checking the board for the eight possible winning combinations. Upon detecting a winning combination, update the winner attribute to reflect the current player (turn).

# A loop of some sort would be appropriate, but you can also check each combination manually:
    def check_for_winner(self):
        winning_combos = [
            ['a1', 'b1', 'c1'],
            ['a2', 'b2', 'c2'],
            ['a3', 'b3', 'c3'],
            ['a1', 'a2', 'a3'],
            ['b1', 'b2', 'b3'],
            ['c1', 'c2', 'c3'],
            ['a1', 'b2', 'c3'],
            ['a3', 'b2', 'c1'],
        ]
        for combo in winning_combos:
            if all([self.board[pos] == self.turn for pos in combo]):
                self.winner = self.turn
                return 
#             Step 6 - Checking for a tie
# The check_for_winner method should be followed with a check_for_tie method.

# This method should check if both of the following conditions are true:

# The board is entire: All spaces on the board are filled, with no positions marked as None.
# No winner: A winner has not already been declared.
# If both of these conditions are met, the value of tie should be set to True.

    def check_for_tie(self):
        if all(self.board[space] is not None for space in self.board) and self.winner is None:
            self.tie = True
# Step 7 - Switching turns
# The switch_turn method should alternate the value of turn between 'X' and 'O'. This should occur at the end of every turn. There are several ways to accomplish this, but a small lookup table using a dictionary might work nicely.
    def switch_turn(self):
        self.turn = 'O' if self.turn == 'X' else 'X'
# Step 8 - Managing gameplay
# The last step is combining all these methods in a functional gameplay loop. The loop should continue until a winner or tie is declared.

# Below is an outline of how you might structure the play_game method:

    def render(self):
        while not self.winner and not self.tie:
            self.print_board()
            self.print_message()
            move = self.get_move()
            self.board[move] = self.turn
            self.check_for_winner()
            self.check_for_tie()
            self.switch_turn()
        self.print_board()
        self.print_message()
 
game_instance = Game()
game_instance.play_game()



