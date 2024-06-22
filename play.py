#THE INTERACTIVE SHELL
#run init commands

from init import Init_list
import chopsticks as cs
import files


def Startup():
    print("Do you want to play a game?")
    while input_string := input("y/n: "):
        if input_string == 'n':
            print("too bad...")
            return 1
        if input_string == 'y':
            print("excellent...")
            return 0
        else:
            print("stoooobid!")
            continue

def Play():
    if Startup() == 1:
        return 0
    position_list = Init_list()
    
    while input_string := input("> "):
        print(input_string)
    return 0
