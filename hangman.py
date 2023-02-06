"""
Simple hangman game
"""

import random

"""Prints:
  ^ ^
 (^_^)
/(   )\
  U U
 """
def print_character_default():
	print("  ^ ^\n (^_^)\n/(   )\\\n  U U")

"""
Prints:
  ^ ^
 (-_-)
/(   )\
  U U
"""
def print_character_miss_1():
	print("  ^ ^\n (-_-)\n/(   )\\\n  U U")

"""
Prints:
  ^ ^
 (-_-)
-(   )-
  U U
"""
def print_character_miss_2():
	print("  ^ ^\n (-_-)\n-(   )-\n  U U")

"""
Prints:
  ^ ^
 (u_u)
 (^ ^)
  U U
"""
def print_character_miss_3():
	print("  ^ ^\n (u_u)\n (^ ^)\n  U U")

"""
Prints:
  ^ ^
 (u_u)
 (^ ^)
  o o
"""
def print_character_miss_4():
	print("  ^ ^\n (u_u)\n (^ ^)\n  o o")

"""
Prints:
  ^ ^
 (o_o)
 (^ ^)
  o o
"""
def print_character_miss_5():
	print("  ^ ^\n (o_o)\n (^ ^)\n  o o")

"""Prints:
  ^ ^
 (^.^)
\(   )/
  U U
  """
def print_character_win():
	print("  ^ ^\n (^.^)\n\\(   )/\n  U U")

"""
Prints:
  Y Y
 (XOX)
\(   )/
  o o
"""
def print_character_lose():
	print("  Y Y\n (XOX)\n\\(   )/\n  o o")

def print_character(num_round_guesses):
	match num_round_guesses:
		case 0:
			print_character_default()
		case 1:
			print_character_miss_1()
		case 2:
			print_character_miss_2()
		case 3:
			print_character_miss_3()
		case 4:
			print_character_miss_4()
		case 5:
			print_character_miss_5()
		case 6:
			print_character_lose()
		case -1:
			print_character_win()
		case _:
			print_character_default()

def print_options():
	pass

def print_game_screen(num_round_guesses):
	print_character(num_round_guesses)
	print_options()
	pass

# Set possible answers
POSSIBLE_ANSWERS = ["The Gay Agenda", "tacos", "Nyan Cat", \
  "Numa Numa Yay", "Badgers and Mushrooms"]
print(POSSIBLE_ANSWERS)

# Set num guesses allowed per round
# Can't be used in a case statement without dot notation
MAX_GUESSES_PER_ROUND = 7

# Randomly select an answer for this round
round_answer = POSSIBLE_ANSWERS[random.randint(0, len(POSSIBLE_ANSWERS)-1)]
print(round_answer)

num_guesses_this_round = 0

# Print un-guessed game screen
# print_game_screen(num_guesses_this_round)
print_game_screen(-1)
print_game_screen(0)
print_game_screen(1)
print_game_screen(2)
print_game_screen(3)
print_game_screen(4)
print_game_screen(5)
print_game_screen(6)

# Ask user to guess a letter, enter the answer, give up, or quit

# Validate input

# Ask user for valid input if not valid

# Send user to answer guessing prompt if selected

# Send user to char guessing prompt if selected

# Reveal answer if user gave up

# Exit if user quit

# Handle correct char guess

# Handle incorrect char guess

# Handle correct answer guess

# Handle incorrect answer guess

# Create win screen

# Create lost screen

# Ask if user wants to play again or quit
# May want a way to prevent repeated words in one session

# Start new game in a way that allows code reuse if selected

# Exit if selected

# Optional later - add colors

# Optional later - add different images to subtract from

# Optional later - add option to import possible answer lists

# Optional later - add option to select difficulty

# Optional later - add ability to view guesses so far
