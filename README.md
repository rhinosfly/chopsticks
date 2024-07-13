# What is it?
- a program to play the chopsticks finger game
# Structure
- chopsticks.py
  - class definition for a single chopsticks position called "Position"
  - methods that act a single Position
  - functions that act a list of Positions
- init.py
  - imports chopsticks
  - functions for initializing list of Positions for a game
    - (make list, fill in values etc.)
- files.py
  - imports chopsticks
  - function for writing all Positions and their links into markdown files for viewing in Obsidian
- shell.py
  - a stand-alone general-use interactive shell based on bash
  - Shell(command_dictionary) can run functions in command_dictionary
- commands.py
  - imports a lot
  - dictionary to be passed to shell
  - corrosponding function definitions
- main.py
  - imports Shell from shell and commands
  - calls Shell(commands.dictionary)
# How to use
