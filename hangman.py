"""
Simple hangman game
"""


# IMPORTS

import random
import re
import ascii_creatures


# FUNCTIONS:

def print_character():
	ascii_creature_printer = ascii_creatures.Ascii_Creatures()
	print("\n")
	# Ref: https://www.freecodecamp.org/news/python-switch-statement-switch-case-example/
	match num_round_guesses:
		case 0:
			ascii_creature_printer.print_character_default()
		case 1:
			ascii_creature_printer.print_character_miss_1()
		case 2:
			ascii_creature_printer.print_character_miss_2()
		case 3:
			ascii_creature_printer.print_character_miss_3()
		case 4:
			ascii_creature_printer.print_character_miss_4()
		case 5:
			ascii_creature_printer.print_character_miss_5()
		case 6:
			ascii_creature_printer.print_character_lose()
		case -1:
			ascii_creature_printer.print_character_win()
		case _:
			ascii_creature_printer.print_character_default()

def print_answer_display():
	print("\nWord or phrase to guess:")
	print(f"{answer_display}\n")

# Ask user to guess a letter, enter the answer, give up, or quit
def print_options_round():
	print("What next?")
	print("1. Guess a letter\n2. Guess answer\n3. Give up round\n4. Quit")

def get_user_option_selection():
	user_input = False
	while user_input == False:
		try:
			print_game_screen()
			selected_option = input('> ')
			selected_option = int(selected_option)
			if selected_option == 1 or selected_option == 2 or \
			 selected_option == 3 or selected_option== 4:
				user_input = True
				return selected_option
			else:
				# TODO: Fix code reuse
				print(f"{selected_option} is not a valid option.")
				print("Please try again.")
		except ValueError:
			print(f"{selected_option} is not a valid option.")
			print("Please try again.")
			continue

def get_from_user_char():
	user_guess = str(input('> '))
	return user_guess

def check_char_against_answer(char_to_check):
	round_answer_lower = round_answer.lower()
	char_to_check_lower = char_to_check.lower()
	if char_to_check_lower in round_answer_lower and \
	 char_to_check not in answer_display:
		return "guessed right"
	elif char_to_check_lower not in round_answer_lower:
		return "guessed wrong"
	elif char_to_check_lower in round_answer_lower and \
	 char_to_check not in answer_display:
		return "already guessed"

# Ref: https://www.w3schools.com/python/python_variables_global.asp#midcontentadcontainer
def update_answer_display(new_answer_display):
	global answer_display
	answer_display = new_answer_display

def get_location_of_matched_chars(guessed_char):
	# Ref: https://stackoverflow.com/questions/11122291/how-to-find-char-in-string-and-get-all-the-indexes#answer-11122355
	match_indeces = [i for i, ltr in enumerate(round_answer) \
	 if ltr.lower() == guessed_char.lower()]
	return match_indeces

def create_new_answer_display_list_of_strings(match_indeces):
	temp_str_list = []
	chars_built_so_far = 0
	# Grabs the current display string up until the next match
	# Adds the newly guessed char where it belongs
	# Stores them in a list of chars
	# Tracks what has already been grabbed so string stays same length
	# Repeats until you have the full string in an array
	for x in match_indeces:
		temp_str_list += answer_display[chars_built_so_far:x] + round_answer[x]
		chars_built_so_far = chars_built_so_far + len(answer_display[chars_built_so_far:x]) + 1
	# If there are trailing chars after the last match,
	# grab them, too
	if len(temp_str_list) < len(answer_display):
		temp_str_list += answer_display[len(temp_str_list):]
	return temp_str_list

def convert_list_of_strings_to_string(str_list):
	new_string = "".join(str_list)
	return new_string

def create_new_answer_display(guessed_char):
	# Figure out where match exists and then update answer_display
	# Careful not to erase previous right answers!
	match_indeces = get_location_of_matched_chars(guessed_char)
	temp_str_list = create_new_answer_display_list_of_strings(match_indeces)
	new_answer_display = convert_list_of_strings_to_string(temp_str_list)
	return new_answer_display

def check_if_round_won():
	if '^' in answer_display:
		return False
	else:
		num_round_guesses_won()
		return True

def check_if_round_lost():
	if MAX_GUESSES_PER_ROUND <= num_round_guesses:
		return True
	else:
		return False

def get_win_status():
	if check_if_round_won() is True:
		return "Won round!"
	elif check_if_round_lost() is True:
		return "Lost round!"
	else:
		return "Current round neither won nor lost."

def num_round_guesses_increment():
	global num_round_guesses
	num_round_guesses += 1

def num_round_guesses_clear():
	global num_round_guesses
	num_round_guesses = 0

def num_round_guesses_won():
	global num_round_guesses
	num_round_guesses = -1

def respond_char_guessed_correct(guessed_char):
	print("\n~~^*^~~^*^~~^*^~~^*^~~")
	print(f"  {guessed_char} is in the answer!")
	print("~~^*^~~^*^~~^*^~~^*^~~")

def respond_char_guessed_wrong():
	print("\n~~^*^~~^*^~~^*^~~^*^~~")
	print("  Nope!")
	print("~~^*^~~^*^~~^*^~~^*^~~")

# Not reachable yet
def respond_char_guessed_duplicate():
	print("\n~~^*^~~^*^~~^*^~~^*^~~")
	print("  You already guessed that right, silly! uwu")
	print("~~^*^~~^*^~~^*^~~^*^~~")

def print_win_message():
	print("You've won this round!!")
	print("Please quit and restart the program to play again! :3")

def print_message_round_lost():
	print("You've lost this round!!")
	print("Please quit and restart the program to play again! :3")

def respond_to_guessed_char(guessed_char, in_answer):
	if in_answer == 'guessed right':
		respond_char_guessed_correct(guessed_char)
		new_answer_display = create_new_answer_display(guessed_char)
		update_answer_display(new_answer_display)
		if get_win_status() == "Won round!":
			print_win_message()
	elif in_answer == 'guessed wrong':
		respond_char_guessed_wrong()
		num_round_guesses_increment()
		if get_win_status() == "Lost round!":
			print_message_round_lost()
	# Not reachable yet
	elif in_answer == "already guessed":
		respond_char_guessed_duplicate()
	return

def guess_char():
	guessed_char = get_from_user_char()
	in_answer = check_char_against_answer(guessed_char)
	respond_to_guessed_char(guessed_char, in_answer)
	return

def print_game_screen():
	print_character()
	print_answer_display()
	print_options_round()


# VARIABLES, GLOBALS ETC

# Set possible answers
global POSSIBLE_ANSWERS
POSSIBLE_ANSWERS = ["The Gay Agenda", "tacos", "Nyan Cat", \
  "Numa Numa Yay", "Badgers and Mushrooms"]

# Set num guesses allowed per round
# Count begins at 0, so 6 means 7 guesses
global MAX_GUESSES_PER_ROUND
MAX_GUESSES_PER_ROUND = 6

# Randomly select an answer for this round
global round_answer
round_answer = POSSIBLE_ANSWERS[random.randint(0, len(POSSIBLE_ANSWERS)-1)]
# Ref: https://flexiple.com/python/python-regex-replace/
global answer_display 
answer_display = re.sub("[A-Za-z]", "^", round_answer)

global num_round_guesses
num_round_guesses_clear() # sets num_round_guesses to 0


# PROGRAM ENTRY POINT

# 1. Guess a letter 2. Guess answer 3. Give up round 4. Quit
while True:
	# Get & validate input
	selected_option = get_user_option_selection()
	# Send user to char guessing prompt if selected
	if selected_option == 1:
		guess_char()
	elif selected_option == 4:
		print("Goodbye!")
		exit()

# Send user to answer guessing prompt if selected

# Reveal answer if user gave up

# Handle correct answer guess

# Ask if user wants to play again or quit
# May want a way to prevent repeated words in one session

# Start new game in a way that allows code reuse if selected

# Optional later - add colors

# Optional later - add different images to subtract from

# Optional later - add option to import possible answer lists

# Optional later - add option to select difficulty

# Optional later - add ability to view guesses so far
