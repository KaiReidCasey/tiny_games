"""
Simple hangman game
"""

import random

# Set possible answers
POSSIBLE_ANSWERS = ["The Gay Agenda", "tacos", "Nyan Cat", \
  "Numa Numa Yay", "Badgers and Mushrooms"]
print(POSSIBLE_ANSWERS)

# Set num guesses allowed per round
MAX_GUESSES_PER_ROUND = 7

# Randomly select an answer for this round
round_answer = POSSIBLE_ANSWERS[random.randint(0, len(POSSIBLE_ANSWERS)-1)]
print(round_answer)

# Print un-guessed game screen - try to make it less grim (flower?)
"""
1.
  ^ ^
 (^_^)
/(   )\
  U U

2.
  ^ ^
 (-_-)
/(   )\
  U U

3.
  ^ ^
 (-_-)
-(   )-
  U U

4.
  ^ ^
 (u_u)
 (^ ^)
  U U

5.
  ^ ^
 (u_u)
 (^ ^)
  o o

6.
  ^ ^
 (o_o)
 (^ ^)
  o o

7.
  Y Y
 (XOX)
\(   )/
  o o

"""

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
