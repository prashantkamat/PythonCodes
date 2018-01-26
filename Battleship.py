#Code credits - www.codeacademy.com

from random import randint

board_game = [] #initialize an empty battleship board game

for x in range(0, 5):
  board_game.append(["O"] * 5)

def print_board(board_game):
  for row in board_game:
    print "-".join(row)

print_board(board_game)

def random_row(board_game):
  return randint(0, len(board_game) - 1)

def random_col(board_game):
  return randint(0, len(board_game[0]) - 1)

ship_row = random_row(board_game)
ship_col = random_col(board_game)
print ship_row
print ship_col


for turn in range(4):
  print "Turn", turn + 1
  guess_row = int(raw_input("Guess Row: "))
  guess_col = int(raw_input("Guess Col: "))

  if guess_row == ship_row and guess_col == ship_col:
    print "Congratulations! You sank my battleship!"
    break
  else:
    if guess_row not in range(5) or \
      guess_col not in range(5):
      print "Oops, that's not even in the ocean."
    elif board_game[guess_row][guess_col] == "X":
      print( "You guessed that one already." )
    else:
      print "You missed my battleship!"
      board_game[guess_row][guess_col] = "X"
    if (turn == 3):
      print "Game Over"
    print_board(board_game)