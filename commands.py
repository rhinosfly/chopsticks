#DICTIONARY OF SHELL COMMANDS


from init import Init_list
import chopsticks as cs
import files


def Startup(arg_list):
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

def Play(arg_list):
    Startup()

def Print(arg_list):
    print('hi')

def Echo(args):
    print(args[1])
    
#dicitonary assigns strings to functions to call from shell
dictionary = {
    "startup" : Startup,
    "print" : Print,
    "echo" : Echo
    }
