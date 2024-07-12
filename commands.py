#DICTIONARY OF SHELL COMMANDS


from init import Init_list
import chopsticks as cs
import files


def Startup():
    print("Do you want to play a game?")
    while True:
        input_string = input("y/n: ")
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
    Startup()

def Print():
    print('hi')

    
#dicitonary assigns strings to functions to call from shell
dictionary = {
    "startup" : Startup,
    "print" : Print
    }
