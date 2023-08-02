# tiny_games

## Hangman

### Description
This is a terminal-based word/phrase guessing game. A cute ASCII character lets you know how you're doing and cheers for you when you win.

### Setup Instructions
- Make a local copy of the tiny_games repository
  - [Follow the instructions here learn how to make a local copy of a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
  - Use the instructions in the link above to clone the game code
  - If you get stuck, [open an issue in the tiny_games repository](https://github.com/KaiReidCasey/tiny_games/issues)
    - Press the green "New Issue" button to the left
    - I will attempt to clarify steps
- Make sure you have Python 3 installed (tiny_games uses Python 3.10.2)
  - `python --version` will tell you if it is installed and which version you have
  - If it is not installed, you can go to [Python's main download page](https://www.python.org/downloads/) for more help, or [Python's 3.10.2 release page](https://www.python.org/downloads/release/python-3102/)
    - Open a new issue as described for cloning the repository locally if you need more help and I will do my best to assist you.
- Navigate to the game
  - Open your Terminal or Command Prompt
    - In Windows:
      - Go to the search bar next to the start menu and type "Command Prompt" without the quotes
      - Select the black box icon for Command Prompt
      - Type cd, then the file path to where you saved tiny_games (ex: `cd Documents\code\GitHub\tiny_games`)
      - Hit the Enter key
- Start the game
  - Type `python hangman.py`
  - Hit the Enter key

### Rules
- You can guess any letter of the English alphabet
- The capitalization of the letter does not matter (`A` and `a` count as the same)
- You have 6 incorrect guesses before you lose
