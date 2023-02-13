"""
Simple hangman game
"""

import random
import re
import ascii_creatures

def print_character(num_round_guesses):
	ascii_creature_printer = ascii_creatures.Ascii_Creatures()
	print("\n")
	# Ref: https://www.freecodecamp.org/news/python-switch-statement-switch-case-example/
	match num_round_guesses:
		case 0:
			ascii_creature_printer.print_character_default() # too many args
			# ascii_creatures.print_character_default() # can't find function
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
			print_game_screen(num_guesses_this_round)
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
	# print(f"char_to_check: {char_to_check}")
	# print(f"round_answer: {round_answer}")
	# print(f"answer_display: {answer_display}")
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

def create_new_answer_display(guessed_char):
	# Figure out where match exists and then update answer_display
	# Careful not to erase previous right answers!
	# Ref: https://stackoverflow.com/questions/11122291/how-to-find-char-in-string-and-get-all-the-indexes#answer-11122355
	match_indeces = [i for i, ltr in enumerate(round_answer) \
	 if ltr.lower() == guessed_char.lower()]
	temp_str_list = []
	chars_built_so_far = 0
	for x in match_indeces:
		temp_str_list += answer_display[chars_built_so_far:x] + round_answer[x]
		chars_built_so_far = chars_built_so_far + len(answer_display[chars_built_so_far:x]) + 1
	if len(temp_str_list) < len(answer_display):
		temp_str_list += answer_display[len(temp_str_list):]
	new_answer_display = "".join(temp_str_list)
	return new_answer_display

def check_if_won():
	if '^' in answer_display:
		return False
	else:
		return True

def check_if_lost():
	# TODO: Make functional
	return False

def get_win_status():
	if check_if_won() is True:
		return "Won round!"
	elif check_if_lost() is True:
		return "Lost round!"
	else:
		return "Current round neither won nor lost."

def guess_char(num_guesses_this_round):
	guessed_char = get_from_user_char()
	in_answer = check_char_against_answer(guessed_char)
	if in_answer == 'guessed right':
		print("\n~~^*^~~^*^~~^*^~~^*^~~")
		print(f"  {guessed_char} is in the answer!")
		print("~~^*^~~^*^~~^*^~~^*^~~")
		new_answer_display = create_new_answer_display(guessed_char)
		update_answer_display(new_answer_display)
		if get_win_status() == "Won round!":
			print("You've won this round!!")
			print("Please quit and restart the program to play again! :3")
	elif in_answer == 'guessed wrong':
		print("\n~~^*^~~^*^~~^*^~~^*^~~")
		print("  Nope!")
		print("~~^*^~~^*^~~^*^~~^*^~~")
		num_guesses_this_round += 1
	# Not reachable yet
	elif in_answer == "already guessed":
		print("\n~~^*^~~^*^~~^*^~~^*^~~")
		print("  You already guessed that right, silly! uwu")
		print("~~^*^~~^*^~~^*^~~^*^~~")
	return num_guesses_this_round

def print_game_screen(num_round_guesses):
	print_character(num_round_guesses)
	print_answer_display()
	print_options_round()
	pass

# Set possible answers
POSSIBLE_ANSWERS = ["The Gay Agenda", "tacos", "Nyan Cat", \
  "Numa Numa Yay", "Badgers and Mushrooms"]
# print(POSSIBLE_ANSWERS)

# Set num guesses allowed per round
# Can't be used in a case statement without dot notation
MAX_GUESSES_PER_ROUND = 7

# Randomly select an answer for this round
round_answer = POSSIBLE_ANSWERS[random.randint(0, len(POSSIBLE_ANSWERS)-1)]
# Ref: https://flexiple.com/python/python-regex-replace/
global answer_display 
answer_display = re.sub("[A-Za-z]", "^", round_answer)

num_guesses_this_round = 0

# 1. Guess a letter 2. Guess answer 3. Give up round 4. Quit
while True:
	# Get & validate input
	selected_option = get_user_option_selection()
	# Send user to char guessing prompt if selected
	if selected_option == 1:
		num_guesses_this_round = guess_char(num_guesses_this_round)
	# Quit game
	elif selected_option == 4:
		print("Goodbye!")
		exit()

# Send user to answer guessing prompt if selected

# Reveal answer if user gave up

# Handle correct answer guess

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
